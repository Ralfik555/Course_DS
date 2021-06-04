import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

#input data
xmin, xmax = -5, 5
n_samples = 100
np.random.seed(0)
X = np.random.normal(size=n_samples)
y = (X > 0).astype(np.float)
X[X > 0] *= 4
X += .3 * np.random.normal(size=n_samples)

#test data
X_test = np.linspace(-5, 10, 300)

#input data chart
plt.figure(1, figsize=(8, 8))
plt.scatter(X, y, color='blue')
plt.ylabel('y')
plt.xlabel('X')
plt.xticks(range(-2, 16))
plt.yticks([0, 0.5, 1])
plt.show()

##### task 1 #####
#linear resgression
lrModel = linear_model.LinearRegression()
X = X[:, np.newaxis]
lrModel.fit(X, y)

#linear refression
plt.figure(1, figsize=(8, 8))
plt.scatter(X.ravel(), y, color='black')
plt.ylabel('y')
plt.xlabel('X')
plt.xticks(range(-5, 10))
plt.yticks([0, 0.5, 1])
plt.plot(X_test, lrModel.coef_ * X_test + lrModel.intercept_, linewidth=1)
plt.show()

##### task 2 #####
#logistic function
def logit(x):
    return 1 / (1 + np.exp(-x))
	
#values of logit(X_test)
Y_test = logit(X_test)

#results chart
plt.figure(1, figsize=(8, 8))
plt.ylabel('y')
plt.xlabel('X')
plt.xticks(range(-10, 10))
plt.yticks([0, 0.5, 1])
plt.plot(X_test, Y_test, linewidth=1)
plt.show()
