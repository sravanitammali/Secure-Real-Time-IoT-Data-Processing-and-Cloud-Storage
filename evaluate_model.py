import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Simulated test data
test = pd.read_csv("s3://iotdevicedatabackup/rcf/train/all_devices_train.csv")

# Load trained model
model = joblib.load("ml_model/isoforest_model.joblib")

# Predict anomalies
pred = model.predict(test)

# Simulated ground truth (all normal except few anomalies)
true_labels = [1 if i % 5 else -1 for i in range(len(pred))]

acc = accuracy_score(true_labels, pred)
prec = precision_score(true_labels, pred, pos_label=-1)
rec = recall_score(true_labels, pred, pos_label=-1)
f1 = f1_score(true_labels, pred, pos_label=-1)

print(f"📊 Accuracy: {acc:.2f}")
print(f"🎯 Precision: {prec:.2f}")
print(f"♻️ Recall: {rec:.2f}")
print(f"🏆 F1 Score: {f1:.2f}")
