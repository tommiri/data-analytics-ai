import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("emp-dep.csv", dtype={"phone1": str, "phone2": str})

agc = pd.DataFrame(df["age_group"].value_counts()).reset_index()

sns.barplot(x="age_group", y="count", data=agc)
plt.show()
