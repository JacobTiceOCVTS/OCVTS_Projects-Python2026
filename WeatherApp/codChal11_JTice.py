import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

hours_studied = [ 15, 12 , 9 , 7 , 5, 5, 4, 3, 1]
scores = [ 98 , 90, 95 , 87 , 84, 80, 78, 74, 65]

X = np.array(hours_studied).reshape(-1, 1)
y = np.array(scores)
model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

new_hours = np.array([[6]])
predicted_score = model.predict(new_hours)
print(f"Predicted score for 6 hours of studying: {predicted_score}")

plt.scatter(X, y)
plt.plot(X, predictions, color="red")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.title("Simple Linear Regression")
plt.show()

