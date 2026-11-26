"""Q12: Line plot of monthly temperature and scatter plot of monthly rainfall."""
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature = [25, 27, 29, 32, 35, 34, 33, 32, 31, 29, 27, 25]          # deg C
rainfall = [20, 10, 15, 25, 50, 55, 90, 120, 130, 250, 350, 150]        # mm

# 1. Line plot of temperature
plt.figure(figsize=(8, 5))
plt.plot(months, temperature, marker="o", color="red")
plt.title("Monthly Temperature - Line Plot")
plt.xlabel("Month"); plt.ylabel("Temperature (°C)"); plt.grid(True)
plt.show()

# 2. Scatter plot of rainfall
plt.figure(figsize=(8, 5))
plt.scatter(months, rainfall, color="blue", s=80)
plt.title("Monthly Rainfall - Scatter Plot")
plt.xlabel("Month"); plt.ylabel("Rainfall (mm)"); plt.grid(True)
plt.show()
