"""Q25: Decision Tree classifier for Iris flower species."""
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)

print(f"Model accuracy on test data: {accuracy_score(y_test, model.predict(X_test)):.2f}\n")

sl = float(input("Enter sepal length (cm): "))
sw = float(input("Enter sepal width (cm): "))
pl = float(input("Enter petal length (cm): "))
pw = float(input("Enter petal width (cm): "))

new_flower = [[sl, sw, pl, pw]]
pred = model.predict(new_flower)[0]
print("Predicted species:", iris.target_names[pred])
