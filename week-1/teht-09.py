import pandas as pd

df = pd.read_csv('diabetes.csv')

countsByAge = df.value_counts('Age')

print(countsByAge)

countsByOutcome = df.value_counts('Outcome')

print(countsByOutcome)
