📂 Log Collector – Fetching & Preprocessing CloudWatch Logs
This module is responsible for fetching real-time logs from AWS CloudWatch, cleaning the data, and preparing it for AI processing.

🚀 1️⃣ fetch_logs.py – Fetch AWS CloudWatch Logs
This script connects to AWS CloudWatch, collects logs, and saves them into a CSV file.

🔹 How It Works:
✅ Connects to AWS using boto3.
✅ Fetches CPU, Memory, Disk, Network, and Error logs for an EC2 instance.
✅ Saves logs into logs/cloudwatch_logs.csv.
python fetch_logs.py
✅ Output:
✅ Logs saved to logs/cloudwatch_logs.csv






🚀 2️⃣ log_preprocessor.py – Clean & Normalize Logs for AI
This script reads raw logs from CloudWatch and prepares them for AI.

🔹 How It Works:
✅ Loads cloudwatch_logs.csv.
✅ Fills missing values (e.g., empty logs become 0).
✅ Normalizes the data (scales values between 0 - 1).
✅ Saves cleaned logs into logs/processed_logs.csv.


python log_preprocessor.py
✅ Output:
✅ Processed logs saved to logs/processed_logs.csv
📌 Why This is Important?
🔥 AI can’t understand raw AWS logs—it needs clean, structured data!
🔥 This module ensures that AI gets the best-quality logs to predict failures accurately!
