"""Q21: Point estimate and confidence interval of mean concentration using NumPy."""
import os
import math
from statistics import NormalDist
import numpy as np

FILE = "rare_elements.csv"
if not os.path.exists(FILE):                       # demo data
    np.savetxt(FILE, np.random.default_rng(3).normal(50, 8, 500), header="concentration", comments="", fmt="%.3f")

data = np.loadtxt(FILE, skiprows=1)
print(f"Population file has {len(data)} measurements")

n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (e.g. 95): ")) / 100
precision = float(input("Enter desired precision (max margin of error): "))

sample = np.random.default_rng().choice(data, size=n, replace=False)

mean = sample.mean()                               # point estimate
std = sample.std(ddof=1)
z = NormalDist().inv_cdf(1 - (1 - confidence) / 2)
margin = z * std / math.sqrt(n)
low, high = mean - margin, mean + margin

print(f"\nPoint estimate (sample mean): {mean:.4f}")
print(f"Sample std deviation        : {std:.4f}")
print(f"{confidence*100:.0f}% confidence interval   : ({low:.4f}, {high:.4f})")
print(f"Margin of error             : {margin:.4f}")

if margin <= precision:
    print(f"Desired precision of {precision} is achieved.")
else:
    needed = math.ceil((z * std / precision) ** 2)
    print(f"Desired precision of {precision} NOT achieved. Sample size needed is about {needed}.")
