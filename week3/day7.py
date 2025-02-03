import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.info())
print(df.describe())


df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Age"].mode()[0])

df = df.drop_duplicates()
first_class = df[df["Pclass"] == 1]
print("First Class Passengers: \n", first_class.head())

# #bar chart
# survival_by_class = df.groupby("Pclass")["Survived"].mean()
# survival_by_class.plot(kind = "bar", color="skyblue")
# plt.title("Survival Rate by Class")
# plt.xlabel("Class")
# plt.ylabel("Survival rate")
# plt.show()

#Histogram 
# sns.histplot(df["Age"], kde=True, bins=20, color="purple")
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="green")
# plt.title("Age vs Fare")
# plt.xlabel("Age")
# plt.ylabel("Fare")
# plt.show()
