import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics

df = pd.read_csv("data/salary.csv")
desc = df.describe()

X = np.array(df["YearsExperience"]).reshape(-1, 1)
y = np.array(df["Salary"]).reshape(-1, 1)

plt.scatter(X, y)
plt.show()

corr = df.corr("pearson")

# Get correlation coefficient and p-value
r, p = pearsonr(df["YearsExperience"], df["Salary"])
print(f"p value = {p}")

sns.heatmap(corr, annot=True)
plt.show()


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

reg = LinearRegression()
# Train model
reg.fit(X_train, y_train)

# Get coefficient and intercept
coef = reg.coef_[0][0]
intercept = reg.intercept_[0]

# Print equation of the line
print(f"y = {coef}x + {intercept}")  # y = 9360.261286193656x + 26777.391341197625

# Predict salaries with test data
test_pred = reg.predict(X_test)

# Plot test data and predictions
plt.scatter(X_test, y_test, color="red")
plt.plot(X_test, test_pred)
plt.show()

# Plot test data with seaborn
sns.regplot(x=X_test, y=y_test)
plt.show()

# Get r2, mean absolute error, mean squared error and root mean squared error
r2 = metrics.r2_score(y_test, test_pred)  # 0.9740993407213511
mae = metrics.mean_absolute_error(y_test, test_pred)  # 3737.417861878896
mse = metrics.mean_squared_error(y_test, test_pred)  # 23370078.800832972
rmse = np.sqrt(mse)  # 4834.260936361728

# Predict salary with 7 years of experience
pred_7years = reg.predict(np.array([[7]]).reshape(-1, 1))
print(f"Salary with 7 years of experience: {pred_7years[0][0]}")
