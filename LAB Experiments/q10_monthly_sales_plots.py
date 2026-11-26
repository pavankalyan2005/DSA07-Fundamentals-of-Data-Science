"""Q10: Line plot and bar plot of monthly sales."""
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [12000, 15000, 14000, 18000, 21000, 19500, 23000, 24500, 22000, 26000, 30000, 34000]

# 1. Line plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o", color="blue")
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month"); plt.ylabel("Sales"); plt.grid(True)
plt.show()

# 2. Bar plot
plt.figure(figsize=(8, 5))
plt.bar(months, sales, color="teal")
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month"); plt.ylabel("Sales")
plt.show()
