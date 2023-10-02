import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create 2D arrays of x and y
X = np.array([1, 2, 3, 4, 6, 7, 8]).reshape(-1, 1)
y = np.array([5, 7, 9, 11, 15, 17, 19]).reshape(-1, 1)

reg = LinearRegression().fit(X, y)

y_pred = reg.predict(np.array([5]).reshape(-1, 1))

plt.plot(X, y, marker="o")
plt.plot(5, y_pred, marker="o", color="red")
plt.show()

print(f"y = {reg.coef_[0][0]}x + {reg.intercept_[0]}")
