"""Q11: Line, scatter and bar plots of sales (with a simple linear trend for prediction)."""
import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 31)
rng = np.random.default_rng(1)
sales = 100 + 3 * days + rng.normal(0, 12, size=30)

# Simple linear prediction (trend line)
slope, intercept = np.polyfit(days, sales, 1)
trend = slope * days + intercept
print(f"Predicted sales on day 31: {slope * 31 + intercept:.2f}")

# 1. Line plot
plt.figure(figsize=(8, 5))
plt.plot(days, sales, marker="o", label="Actual sales")
plt.plot(days, trend, "r--", label="Trend (prediction)")
plt.title("Daily Sales in a Month - Line Plot")
plt.xlabel("Day"); plt.ylabel("Sales"); plt.legend(); plt.grid(True)
plt.show()

# 2. Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(days, sales, color="green", label="Actual sales")
plt.plot(days, trend, "r--", label="Trend (prediction)")
plt.title("Daily Sales in a Month - Scatter Plot")
plt.xlabel("Day"); plt.ylabel("Sales"); plt.legend()
plt.show()

# 3. Bar plot of monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly_sales = [12000, 15000, 14000, 18000, 21000, 19500, 23000, 24500, 22000, 26000, 30000, 34000]
plt.figure(figsize=(8, 5))
plt.bar(months, monthly_sales, color="orange")
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month"); plt.ylabel("Sales")
plt.show()
