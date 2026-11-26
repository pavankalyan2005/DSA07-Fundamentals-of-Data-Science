"""Q23: Hypothesis test (treatment vs placebo), p-value, visualised with matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(11)
placebo = rng.normal(loc=5, scale=3, size=40)       # replace with real data
treatment = rng.normal(loc=8, scale=3, size=40)

# H0: no difference in mean effect   H1: means differ
t_stat, p_value = stats.ttest_ind(treatment, placebo)
alpha = 0.05
dof = len(placebo) + len(treatment) - 2

print(f"t-statistic = {t_stat:.4f}")
print(f"p-value     = {p_value:.6f}")
print("Result:", "Reject H0 - treatment has a significant effect" if p_value < alpha
      else "Fail to reject H0 - no significant effect")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: data comparison
axes[0].boxplot([placebo, treatment])
axes[0].set_xticklabels(["Placebo", "Treatment"])
axes[0].set_title("Patient response by group")
axes[0].set_ylabel("Response")

# Plot 2: t-distribution with the p-value region
x = np.linspace(-6, 6, 500)
y = stats.t.pdf(x, dof)
axes[1].plot(x, y, "k")
crit = stats.t.ppf(1 - alpha / 2, dof)
axes[1].fill_between(x, y, where=(abs(x) >= crit), color="red", alpha=0.3, label=f"Rejection region (α={alpha})")
axes[1].axvline(t_stat, color="blue", linestyle="--", label=f"t = {t_stat:.2f}")
axes[1].set_title(f"t-distribution, p-value = {p_value:.4g}")
axes[1].set_xlabel("t"); axes[1].legend()

plt.tight_layout()
plt.show()
