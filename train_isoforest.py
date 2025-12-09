import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest

# Load your training data (from S3 or local)
data = pd.read_csv("s3://iotdevicedatabackup/rcf/train/all_devices_train.csv")
print("✅ Data loaded for training:", data.shape)

# Train model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(data)

# Save model
joblib.dump(model, "ml_model/isoforest_model.joblib")
print("🎯 Model trained and saved as ml_model/isoforest_model.joblib")
