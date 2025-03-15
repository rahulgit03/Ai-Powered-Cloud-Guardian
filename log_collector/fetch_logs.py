import boto3
import pandas as pd
from datetime import datetime, timedelta

# AWS CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name="us-east-1")  # Change region if needed

# Define the instance ID (replace with your actual EC2 instance ID)
INSTANCE_ID = "i-xxxxxxxxxxxxxxxxx"

# Metrics to fetch
METRICS = [
    {"name": "CPUUtilization", "namespace": "AWS/EC2"},
    {"name": "DiskReadOps", "namespace": "AWS/EC2"},
    {"name": "DiskWriteOps", "namespace": "AWS/EC2"},
    {"name": "NetworkIn", "namespace": "AWS/EC2"},
    {"name": "NetworkOut", "namespace": "AWS/EC2"}
]

# Time range (last 10 minutes)
end_time = datetime.utcnow()
start_time = end_time - timedelta(minutes=10)

# Function to fetch metrics
def get_metric(metric_name, namespace):
    response = cloudwatch.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric_name,
        Dimensions=[{"Name": "InstanceId", "Value": INSTANCE_ID}],
        StartTime=start_time,
        EndTime=end_time,
        Period=60,
        Statistics=["Average"]
    )
    
    data_points = response.get("Datapoints", [])
    return data_points[-1]["Average"] if data_points else None

# Fetch data
log_data = {"Timestamp": [start_time]}
for metric in METRICS:
    log_data[metric["name"]] = [get_metric(metric["name"], metric["namespace"])]

# Convert to DataFrame
df = pd.DataFrame(log_data)

# Save logs to CSV
csv_filename = "logs/cloudwatch_logs.csv"
df.to_csv(csv_filename, index=False)
print(f"✅ Logs saved to {csv_filename}")

