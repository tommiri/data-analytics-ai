import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

df_emp = pd.read_csv('employees.csv', dtype={'phone1':str, 'phone2':str})
df_dep = pd.read_csv('departments.csv')

df = pd.merge(df_emp, df_dep, how='left', on='dep')

print(df['salary'].nlargest(n=5))

desc = df.describe()

df['age'] = (datetime.now() - pd.to_datetime(df['bdate'])) // timedelta(days=365.2425)

bins = list(range(15, 75, 5))

# for i in range(15, 75, 5):
#     bins.append(i)
    
labels = bins[1:] # kopioidaan bins ja otetaan ensimmäinen pois

df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False).astype(int)

# df['age_group'] = df['age_group'].astype(int)

m_count = sum(df.gender==0)
f_count = sum(df.gender==1)

emp_count = df.shape[0]

f_pros = round(f_count / emp_count * 100, 1)
m_pros = round(m_count / emp_count * 100, 1)
