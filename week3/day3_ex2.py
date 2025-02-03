# https://github.com/mwaskom/seaborn-data/blob/master/iris.csv

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# print("First 5 rows", df.head())
# print("Last 5 rows", df.tail())

# print(df.info())

# print(df.describe())

selected_columns = df[["species", "sepal_length"]]
print("Selected columsn: \n", selected_columns)

filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("filtered rows: \n", filtered_rows)