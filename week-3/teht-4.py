import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("titanic.csv")

bins = list(range(0, 95, 5))
labels = bins[1:]
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)

agc = pd.DataFrame(df["AgeGroup"].value_counts()).reset_index()

df.drop(df.loc[df["PClass"] == "*"].index, inplace=True)  # Poistetaan PClass '*'
df["Saved"] = df["Survived"].apply(lambda x: "no" if x == 0 else "yes")

sns.boxplot(x="PClass", y="Age", hue="Saved", data=df)
plt.show()

df_females = df.loc[df["Gender"] == "female"]

ax = sns.stripplot(x="PClass", y="Age", hue="Saved", data=df_females)
ax.set_title("females")
plt.show()

df_males = df.loc[df["Gender"] == "male"]

ax = sns.stripplot(x="PClass", y="Age", hue="Saved", data=df_males)
ax.set_title("males")
plt.show()
