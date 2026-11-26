"""Q14: Frequency distribution of customer ages."""
import pandas as pd

sales_data = pd.DataFrame({
    "customer_id": range(1, 21),
    "age": [23, 25, 31, 25, 42, 31, 23, 35, 29, 25, 42, 31, 50, 35, 23, 29, 31, 42, 25, 35],
    "purchase": [1] * 20,
})

buyers = sales_data[sales_data["purchase"] == 1]

# Frequency of each exact age
print("Frequency of each age:\n")
print(buyers["age"].value_counts().sort_index())

# Frequency by age group
bins = [0, 20, 30, 40, 50, 100]
labels = ["<=20", "21-30", "31-40", "41-50", ">50"]
groups = pd.cut(buyers["age"], bins=bins, labels=labels)
print("\nFrequency by age group:\n")
print(groups.value_counts().sort_index())
