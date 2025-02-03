# https://github.com/mwaskom/seaborn-data/blob/master/iris.csv

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

print("First 5 rows", df.head())
print("Last 5 rows", df.tail())

print(df.info())

print(df.describe())