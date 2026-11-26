"""Q8: Top 5 best-selling products in the past month."""
import pandas as pd

sales_data = pd.DataFrame({
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam", "Mouse", "Laptop",
                "Headset", "Keyboard", "Mouse", "Dock", "Monitor", "Headset", "Mouse"],
    "quantity": [2, 10, 5, 3, 4, 8, 1, 6, 7, 5, 2, 2, 3, 4],
    "date": pd.to_datetime(["2024-05-02", "2024-05-03", "2024-05-04", "2024-05-06", "2024-05-08",
                            "2024-05-10", "2024-05-12", "2024-05-14", "2024-05-16", "2024-05-18",
                            "2024-05-20", "2024-05-22", "2024-05-25", "2024-05-28"]),
})

# Filter to the past month (last 30 days of the data)
last_month = sales_data[sales_data["date"] >= sales_data["date"].max() - pd.Timedelta(days=30)]

top5 = (last_month.groupby("product")["quantity"].sum()
        .sort_values(ascending=False).head(5))
print("Top 5 products sold the most:\n")
print(top5)
