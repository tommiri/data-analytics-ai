import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("emp-dep.csv", dtype={"phone1": str, "phone2": str})

plt.scatter(x=df["age"], y=df["salary"])
plt.show()

# Oma hahmottelu ennen opettajan esimerkkiä
# deps = list(df['dname'].unique())
# employees = []

# for dep in deps:
#     employees.append(df[df['dname'] == dep].shape[0])

# plt.bar(deps, employees)
# plt.show()

df_counts = pd.DataFrame(df["dname"].value_counts()).reset_index()
# df_counts.columns = ['dname', 'count']

df_counts = df_counts.sort_values("dname")

sns.barplot(x="dname", y="count", data=df_counts)
plt.show()
sns.barplot(y="dname", x="count", data=df_counts)
plt.show()
