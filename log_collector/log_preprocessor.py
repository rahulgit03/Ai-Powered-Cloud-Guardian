import pandas as pd

# Load the raw logs
raw_logs_file = "logs/cloudwatch_logs.csv"
df = pd.read_csv(raw_logs_file)

# Fill missing values with 0 (or choose another strategy)
df.fillna(0, inplace=True)

# Normalize numerical values (scale between 0 and 1)
for column in df.columns:
    if column != "Timestamp":
        df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min() + 1e-7)

# Save cleaned & processed logs
processed_logs_file = "logs/processed_logs.csv"
df.to_csv(processed_logs_file, index=False)

print(f"✅ Processed logs saved to {processed_logs_file}")

