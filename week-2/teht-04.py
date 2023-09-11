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

m_count = sum(df['GenderCode'] == 0)
f_count = sum(df['GenderCode'] == 1)

age_mean = df['Age'].mean()

age_zero_count = sum(df['Age'] == 0)

nonzero_age_mean = df['Age'].where(df['Age'] != 0).mean()
df.loc[df['Age'] == 0, 'Age'] = nonzero_age_mean

print(df['PClass'].unique())

pclass_star = df.loc[df['PClass'] == '*']

count_survivors = sum(df['Survived'] == 1)
count_losses = sum(df['Survived'] == 0)

survivors_pros = round(count_survivors / passenger_count * 100, 1)
losses_pros = round(count_losses / passenger_count * 100, 1)

print('Survivors: {}%, Losses: {}%'.format(survivors_pros, losses_pros))

count_survivors_m = sum(df.where(df['GenderCode'] == 0)['Survived'] == 1)
count_survivors_f = sum(df.where(df['GenderCode'] == 1)['Survived'] == 1)
count_losses_m = sum(df.where(df['GenderCode'] == 0)['Survived'] == 0)
count_losses_f = sum(df.where(df['GenderCode'] == 1)['Survived'] == 0)
