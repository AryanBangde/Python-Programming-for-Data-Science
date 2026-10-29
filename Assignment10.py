
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Create dataset
# X = Hours Studied, y = Marks Scored
X = np.array([[1], [2], [3], [4], [5],
              [6], [7], [8], [9], [10]])

y = np.array([35, 42, 50, 58, 65,
              71, 78, 83, 90, 96])

# 2. Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predict marks for test data
y_pred = model.predict(X_test)

# 5. Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Marks per hour (Slope):", round(model.coef_[0], 2))
print("Base marks (Intercept):", round(model.intercept_, 2))
print("Mean Squared Error (MSE):", round(mse, 2))
print("R2 Score:", round(r2, 4))

# 6. Predict marks for 7.5 hours of study
new_hours = np.array([[7.5]])
predicted_marks = model.predict(new_hours)

print("Predicted Marks for 7.5 hours:",
      round(predicted_marks[0], 1), "/100")
