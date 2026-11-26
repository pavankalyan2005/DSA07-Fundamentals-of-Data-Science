"""Q18: Age and %fat - descriptive stats, boxplots, scatter plot, q-q plot."""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
df = pd.DataFrame({"age": age, "%fat": fat})

# 1. Mean, median, standard deviation
print("Mean:\n", df.mean(), "\n")
print("Median:\n", df.median(), "\n")
print("Standard deviation:\n", df.std(), "\n")

# 2. Boxplots
df.plot(kind="box", subplots=True, layout=(1, 2), figsize=(8, 5), title="Boxplots")
plt.suptitle("Boxplots of age and %fat")
plt.show()

# 3a. Scatter plot
plt.figure(figsize=(6, 5))
plt.scatter(df["age"], df["%fat"], color="red")
plt.title("Scatter plot: age vs %fat")
plt.xlabel("age"); plt.ylabel("%fat"); plt.grid(True)
plt.show()

# 3b. q-q plot (quantiles of age vs quantiles of %fat)
q = np.linspace(0, 100, len(df))
plt.figure(figsize=(6, 5))
plt.scatter(np.percentile(df["age"], q), np.percentile(df["%fat"], q), color="blue")
lims = [min(age + fat), max(age + fat)]
plt.plot(lims, lims, "k--", label="y = x")
plt.title("q-q plot: age vs %fat")
plt.xlabel("age quantiles"); plt.ylabel("%fat quantiles"); plt.legend(); plt.grid(True)
plt.show()

# 3c. Normal q-q plots of each variable
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
stats.probplot(df["age"], dist="norm", plot=axes[0]); axes[0].set_title("Normal q-q: age")
stats.probplot(df["%fat"], dist="norm", plot=axes[1]); axes[1].set_title("Normal q-q: %fat")
plt.tight_layout()
plt.show()
