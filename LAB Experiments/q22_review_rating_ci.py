"""Q22: Confidence interval for the true mean rating using pandas."""
import os
import numpy as np
import pandas as pd
from scipy import stats

FILE = "customer_reviews.csv"
if not os.path.exists(FILE):                       # demo data
    ratings = np.random.default_rng(5).choice([1, 2, 3, 4, 5], size=200, p=[.05, .1, .15, .4, .3])
    pd.DataFrame({"rating": ratings}).to_csv(FILE, index=False)

df = pd.read_csv(FILE)
ratings = df["rating"]

n = ratings.count()
mean = ratings.mean()
sem = ratings.sem()                                # std / sqrt(n)

confidence = 0.95
low, high = stats.t.interval(confidence, df=n - 1, loc=mean, scale=sem)

print(f"Number of reviews : {n}")
print(f"Average rating    : {mean:.3f}")
print(f"{confidence*100:.0f}% CI for true mean rating: ({low:.3f}, {high:.3f})")
print(f"Satisfied customers (rating >= 4): {(ratings >= 4).mean()*100:.1f}%")
