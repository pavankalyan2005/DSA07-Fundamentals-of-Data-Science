"""Q24: KNN classifier to predict whether a patient has a medical condition."""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Sample labelled dataset (replace with your own CSV: df = pd.read_csv("patients.csv"))
rng = np.random.default_rng(0)
n = 200
condition = rng.integers(0, 2, n)
df = pd.DataFrame({
    "fever":       np.where(condition == 1, rng.normal(38.5, 0.6, n), rng.normal(36.9, 0.4, n)),
    "cough_score": np.where(condition == 1, rng.normal(7, 1.5, n),    rng.normal(3, 1.5, n)),
    "fatigue":     np.where(condition == 1, rng.normal(6, 2, n),      rng.normal(3, 2, n)),
    "age":         rng.integers(18, 80, n),
    "condition":   condition,
})

X = df.drop(columns="condition")
y = df["condition"]
scaler = StandardScaler()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train_s = scaler.fit_transform(X_train)

# User input
k = int(input("Enter k (number of neighbors): "))
print("Enter patient features:")
features = [float(input(f"  {col}: ")) for col in X.columns]

knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_s, y_train)
print(f"\nModel accuracy on test data: {accuracy_score(y_test, knn.predict(scaler.transform(X_test))):.2f}")

new_patient = scaler.transform(pd.DataFrame([features], columns=X.columns))
pred = knn.predict(new_patient)[0]
print("Prediction:", "Patient HAS the condition (1)" if pred == 1 else "Patient does NOT have the condition (0)")
