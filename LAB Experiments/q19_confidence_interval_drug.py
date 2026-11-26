"""Q19: 95% CI for mean BP reduction - drug vs placebo (25 patients each)."""
import numpy as np
from scipy import stats

# Replace with your real trial data
rng = np.random.default_rng(42)
drug = rng.normal(loc=12, scale=4, size=25)       # reduction in BP (mmHg)
placebo = rng.normal(loc=4, scale=4, size=25)

def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    sem = stats.sem(data)                          # s / sqrt(n)
    low, high = stats.t.interval(confidence, df=n - 1, loc=mean, scale=sem)
    return mean, low, high

for name, data in [("Drug", drug), ("Placebo", placebo)]:
    mean, low, high = confidence_interval(data)
    print(f"{name:8}: mean reduction = {mean:.2f} mmHg, 95% CI = ({low:.2f}, {high:.2f})")
