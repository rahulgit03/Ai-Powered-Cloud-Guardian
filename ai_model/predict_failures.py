import pandas as pd
import joblib

# Load the trained AI model
model = joblib.load("failure_prediction_model.pkl")

# Load new system logs for prediction
df = pd.read_csv("../logs/processed_logs.csv")

# Drop Timestamp (not needed for prediction)
df = df.drop(columns=["Timestamp"])

# Predict failures (0 = Safe, 1 = Failure)
predictions = model.predict(df)

# Add predictions to the dataframe
df["Failure_Predicted"] = predictions

# Save predictions
df.to_csv("../logs/failure_predictions.csv", index=False)
print("✅ Predictions saved to 'logs/failure_predictions.csv'")

# Check if any failures are predicted
if 1 in predictions:
    print("🚨 WARNING: Potential failure detected! Take action immediately! 🚨")
else:
    print("✅ System is running normally. No failures detected.")
