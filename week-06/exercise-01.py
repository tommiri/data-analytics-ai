import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
import sklearn.metrics as metrics

df = pd.read_csv("data/startup.csv")

# Split data to x and y
X = df.drop("Profit", axis=1)
y = df["Profit"]

# Generate dummies using pandas
# state_dummies = pd.get_dummies(X["State"], drop_first=True)
# X = X.drop("State", axis=1)
# X = pd.concat([X, state_dummies], axis=1)

# Generate dummies using sklearn
ct = make_column_transformer(
    (OneHotEncoder(drop="first"), ["State"]), remainder="passthrough"
)
X = ct.fit_transform(X)

# Split data to training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Get coefficient and intercept
coef = model.coef_
intercept = model.intercept_

# Print line equation
print(
    f"y = {intercept} + {coef[0]}*x1 + {coef[1]}*x2 + {coef[2]}*x3 + {coef[3]}*D1 + {coef[4]}*D2"
)

# Test model with test data
test_pred = model.predict(X_test)

# Calculate metrics
r2 = metrics.r2_score(y_test, test_pred)
mae = metrics.mean_absolute_error(y_test, test_pred)
rmse = metrics.mean_squared_error(y_test, test_pred, squared=False)
