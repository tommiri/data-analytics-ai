import pandas as pd

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
sal_avg = df.salary.mean()

tuotekehitys = df[df['dname'] == 'Tuotekehitys'].salary.mean()