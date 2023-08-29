import pandas as pd

df = pd.read_csv('diabetes.csv')

desc = df.describe()

df[['Pregnancies', 'Glucose', 'BloodPressure']].hist()

diabetes = df['Outcome'].value_counts()