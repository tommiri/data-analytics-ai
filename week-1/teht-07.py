import pandas as pd

df = pd.read_csv('diabetes.csv')

desc = df.describe()

print(desc)

df.hist()
