import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('emp-dep.csv', dtype={'phone1': str, 'phone2': str})

plt.scatter(x=df['age'], y=df['salary'])
plt.show()