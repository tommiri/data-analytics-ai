import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')

corr = df.corr()

sns.heatmap(corr, annot=True, cbar=False)
plt.show()
