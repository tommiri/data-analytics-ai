import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns

df_emp = pd.read_csv('employees.csv', dtype={'phone1':str, 'phone2':str})
df_dep = pd.read_csv('departments.csv')

df = pd.merge(df_emp, df_dep, how='inner', on='dep')
df = df.drop(columns=['image'])

emp_count = df.shape[0]

m_count = sum(df.gender==0)
f_count = sum(df.gender==1)

f_pros = round(f_count / emp_count * 100, 1)
m_pros = round(m_count / emp_count * 100, 1)

sal_min = df.salary.min()
sal_max = df.salary.max()
sal_mean = df.salary.mean()

tuotekehitys_sal_mean = df.loc[df['dname'] == 'Tuotekehitys', 'salary'].mean()

no_second_phone = df['phone2'].isna().sum()

df['age'] = (datetime.now() - pd.to_datetime(df['bdate'])) // timedelta(days=365.2425)

bins = list(range(15, 75, 5))
labels = bins[1:]
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

df_new = df[['salary', 'age', 'gender']]

corr = df_new.corr()
corr_heatmap = sns.heatmap(corr, annot=True)