import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("../dataset/cloud_failure_dataset.csv")

# Drop Timestamp (not needed for AI training)
df = df.drop(columns=["Timestamp"])

# Split features (X) and target (y)
X = df.drop(columns=["Failure"])  # All system metrics
y = df["Failure"]  # Target variable (0 = Normal, 1 = Failure)

# Split into Training & Testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train AI Model (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Trained Successfully! Accuracy: {accuracy * 100:.2f}%")

# Save the Trained Model
joblib.dump(model, "failure_prediction_model.pkl")
print("✅ Model saved as 'failure_prediction_model.pkl'")
