import pandas as pd
import matplotlib.pyplot as plt

df_titanic_data = pd.read_csv('Titanic_data.csv')
df_titanic_names = pd.read_csv('Titanic_names.csv')

print(df_titanic_data.info())
print(df_titanic_data.describe())
print(df_titanic_names.info())
print(df_titanic_names.describe())

data_hist = df_titanic_data.hist(bins=4)

df = pd.merge(df_titanic_data, df_titanic_names, how='inner', on='id')
passenger_count = df.shape[0]

m_count = sum(df.GenderCode == 0)
f_count = sum(df.GenderCode == 1)

age_mean = df.Age.mean()

age_zero_count = sum(df.Age == 0)