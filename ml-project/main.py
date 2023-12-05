import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics

# Read the data
df = pd.read_csv("data/housing_price_dataset.csv")

# Explore the data
# df.describe()
# df.head()
# df.info()
df.isnull().sum()

X = df.drop("Price", axis=1)
y = df["Price"]

# Generate dummy variables
neighborhood_dummies = pd.get_dummies(X["Neighborhood"], drop_first=True)
X = X.drop("Neighborhood", axis=1)
X = pd.concat([X, neighborhood_dummies], axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
test_pred = model.predict(X_test)

# Calculate metrics
r2 = metrics.r2_score(y_test, test_pred)
mae = metrics.mean_absolute_error(y_test, test_pred)
rmse = metrics.mean_squared_error(y_test, test_pred, squared=False)
