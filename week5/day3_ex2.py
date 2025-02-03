import pandas as pd
from scipy import stats
import numpy as np

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

sample = df["sepal_length"].sample(30, random_state=42)

mean = np.mean(sample)
std = np.std(sample, ddof=1)
n = len(sample)

z_value = stats.norm.ppf(0.975)
margin_of_error = z_value * (std / np.sqrt(n))
ci = (mean - margin_of_error, mean + margin_of_error)

print("Sample Mean: ", mean)
print("Confidence interval: ", ci)