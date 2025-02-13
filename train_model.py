import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset (Ensure 'beam_failure_data.csv' exists in your project folder)
df = pd.read_csv("beam_failure_data.csv")

# Separate features and labels
X = df.drop(columns=["failure"])  # Features (remove the target column)
y = df["failure"]  # Target variable

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "beam_failure_model.pkl")

print("✅ Model trained and saved as 'beam_failure_model.pkl'")
