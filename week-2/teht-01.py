import pandas as pd

df_emp = pd.read_csv('employees.csv', dtype={'phone1':str, 'phone2':str})
df_dep = pd.read_csv('departments.csv')

emp_desc = df_emp.describe()
dep_desc = df_dep.describe()

df = pd.merge(df_emp, df_dep, how='inner', on='dep')
df = df.drop(columns=['image'])