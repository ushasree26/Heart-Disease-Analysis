import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv("heart_disease.csv")

# Convert text columns to numbers
le = LabelEncoder()

for column in data.columns:
    if data[column].dtype == "object":
        data[column] = le.fit_transform(data[column])

# Split features and target
X = data.drop("HeartDisease", axis=1)
y = data["HeartDisease"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save trained model
joblib.dump(model, "heart_model.pkl")

print("Model trained successfully!")