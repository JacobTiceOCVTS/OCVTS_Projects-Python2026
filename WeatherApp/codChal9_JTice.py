import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

time_practiced =     [0, 2, 5, 7, 10, 15, 17, 19, 26, 30]
game_points_scored = [17, 29, 41, 56, 70, 78, 84, 97, 109, 122]

X = np.array(time_practiced).reshape(-1, 1)
y = np.array(game_points_scored)

model = LinearRegression()
model.fit(X, y)

print(f"Slope of linear regression = ", model.coef_)
print(f"Intercept of linear regression", model.intercept_)

print(f"Predicted number of game points for 13 hours practiced: ", model.predict([[13]]))


predictions = model.predict(X)
plt.scatter(X, y)
plt.plot(X, predictions, color="red")
plt.show()


##### QUESTIONS #####

#question 1:
# .fit() for LinearReg takes two array-like inputs and calculates a line 
# of best fit for predicting new data, it has an intercept and a slope

#question 2
#Sci-kit learn expects a 2d array for the X because it doesn't know if your samples have multiple features.
#Reshaping the array causes it to explicitly have 1 feature and multiple samples
# ex: [1, 2, 3, 4] becomes:
                            #[[1], 
                            # [2], 
                            # [3], 
                            # [4]]

#question 3
#overfitting is when a model basically "memorizes" the data instead of learning the patterns
#this can be analagous to someone memorizing the numbers of a math problem instead of 
#learning to apply formulas that apply to multiple problems