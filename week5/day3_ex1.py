import numpy as np
from scipy import stats

data = np.random.normal(loc=50, scale=10, size=100)


mean = np.mean(data)
std = np.std(data, ddof=1)
n = len(data)

z_value = stats.norm.ppf(0.975)
margin_of_error = z_value * (std / np.sqrt(n))
ci = (mean - margin_of_error, mean + margin_of_error)

print("Sample Mean: ", mean)
print("Confidence interval: ", ci)


