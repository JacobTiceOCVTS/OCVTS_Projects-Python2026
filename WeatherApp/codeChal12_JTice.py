import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

scores = [40, 50, 60, 65 , 70 , 70, 75, 85, 90, 95]
hours_studied = [0, 1, 2, 2, 3, 4, 4, 5, 7, 9]

X = np.array(hours_studied).reshape(-1, 1)
y = np.array([1 if score >= 75 else 0 for score in scores])
model = LogisticRegression()
model.fit(X, y)

X_range = np.linspace(0, 12, 100).reshape(-1, 1)
y_prob = model.predict_proba(X_range)[:, 1]

plt.scatter(X, y)
plt.plot(X_range, y_prob, color="red", label="Predicted Probability")
plt.xlabel("Hours studied")
plt.ylabel("Scores")
plt.legend()
plt.show()

print(f"Likelyhood of passing with 5 hours of studying: {model.predict_proba([[5]])}")