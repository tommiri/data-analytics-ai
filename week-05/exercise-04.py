import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics

df = pd.read_csv("data/housing.csv")

# Separate important data from dataframe
df_new = df[["median_income", "median_house_value"]]
df_new.describe()

X = np.array(df_new["median_income"]).reshape(-1, 1)
y = np.array(df_new["median_house_value"]).reshape(-1, 1)

plt.scatter(X, y)
plt.show()

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

reg = LinearRegression()
# Train model
reg.fit(X_train, y_train)

# Get coefficient and intercept
coef = reg.coef_[0][0]
intercept = reg.intercept_[0]

# Print equation of the line
print(f"y = {coef}x + {intercept}")

# Predict house values with test data
test_pred = reg.predict(X_test)

# Visualize predicted versus actual values with a histogram
plt.hist(y_test, bins=20, alpha=0.5, label="Actual")
plt.hist(test_pred, bins=20, alpha=0.5, label="Predicted")
plt.xlabel("Median House Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

r2 = metrics.r2_score(y_test, test_pred)  # 0.4466846804895944
mae = metrics.mean_absolute_error(y_test, test_pred)  # 63521.30348040669
mse = metrics.mean_squared_error(y_test, test_pred)  # 7214982234.0146055
rmse = np.sqrt(mse)  # 84941.05152406936

# Predict house value for median income of $30,000
pred_30k = reg.predict(np.array(3.0).reshape(-1, 1))
print(f"Predicted house value for median income of $30,000: ${pred_30k[0][0]}")
