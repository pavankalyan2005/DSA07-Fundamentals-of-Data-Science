"""Q20: A/B test - is there a significant difference in mean conversion rates?"""
import numpy as np
from scipy import stats

# Replace with your real daily conversion rates (%)
rng = np.random.default_rng(7)
design_a = rng.normal(loc=10.0, scale=1.5, size=30)
design_b = rng.normal(loc=11.2, scale=1.5, size=30)

print(f"Mean conversion A: {design_a.mean():.3f}")
print(f"Mean conversion B: {design_b.mean():.3f}")

# H0: mean_A == mean_B   H1: mean_A != mean_B   (Welch two-sample t-test)
t_stat, p_value = stats.ttest_ind(design_a, design_b, equal_var=False)
alpha = 0.05
print(f"\nt-statistic = {t_stat:.4f}, p-value = {p_value:.4f}")

if p_value < alpha:
    print("Reject H0: there IS a statistically significant difference between designs A and B.")
else:
    print("Fail to reject H0: no statistically significant difference between designs A and B.")
