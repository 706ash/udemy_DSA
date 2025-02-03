import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Scores": [85, 90, 88]
})

print(f"Dataset 1: \n{df1}")
print(f"\nDataset 2: \n{df2}")

merged = pd.merge(df1, df2, how = "inner", on="ID")
print(f"Merged DS: \n{merged}")

merged["Score_Percentage"] = (merged["Scores"] / 100) * 100
print(f"Transfored DS: \n{merged}")

