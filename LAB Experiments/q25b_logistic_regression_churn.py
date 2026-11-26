"""Q25 (second part): Logistic regression to predict customer churn."""
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Sample dataset (replace with your own: df = pd.read_csv("churn.csv"))
rng = np.random.default_rng(2)
n = 300
usage = rng.normal(300, 100, n).clip(10)          # usage minutes per month
contract = rng.integers(1, 25, n)                 # contract duration in months
score = -0.01 * (usage - 300) - 0.15 * (contract - 12) + rng.normal(0, 1, n)
churn = (score > 0).astype(int)
df = pd.DataFrame({"usage_minutes": usage, "contract_duration": contract, "churn": churn})

X, y = df[["usage_minutes", "contract_duration"]], df["churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

scaler = StandardScaler()
model = LogisticRegression().fit(scaler.fit_transform(X_train), y_train)
print(f"Model accuracy on test data: {accuracy_score(y_test, model.predict(scaler.transform(X_test))):.2f}\n")

usage_in = float(input("Enter usage minutes: "))
contract_in = float(input("Enter contract duration (months): "))

new_customer = scaler.transform(pd.DataFrame([[usage_in, contract_in]], columns=X.columns))
pred = model.predict(new_customer)[0]
prob = model.predict_proba(new_customer)[0][1]
print(f"\nChurn probability: {prob:.2f}")
print("Prediction:", "Customer WILL churn" if pred == 1 else "Customer will NOT churn")
