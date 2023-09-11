import pandas as pd

df = pd.read_csv('diabetes.csv')

invalidValues = df.isnull().sum()

print(invalidValues)
