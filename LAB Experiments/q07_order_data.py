"""Q7: Pandas operations on order_data."""
import pandas as pd

order_data = pd.DataFrame({
    "customer_id": [101, 102, 101, 103, 102, 101, 104, 103],
    "order_date": pd.to_datetime(["2024-01-05", "2024-01-07", "2024-01-12", "2024-02-01",
                                  "2024-02-10", "2024-02-15", "2024-03-02", "2024-03-09"]),
    "product_name": ["Pen", "Book", "Pen", "Bag", "Book", "Bag", "Pen", "Book"],
    "order_quantity": [10, 2, 5, 1, 3, 2, 7, 4],
})
print(order_data, "\n")

# 1. Total number of orders by each customer
print("1. Orders per customer:\n", order_data.groupby("customer_id").size(), "\n")

# 2. Average order quantity per product
print("2. Average quantity per product:\n", order_data.groupby("product_name")["order_quantity"].mean(), "\n")

# 3. Earliest and latest order dates
print("3. Earliest order date:", order_data["order_date"].min().date())
print("   Latest order date  :", order_data["order_date"].max().date())
