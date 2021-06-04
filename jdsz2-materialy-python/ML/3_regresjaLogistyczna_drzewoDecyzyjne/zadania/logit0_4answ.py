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

##### task 1 #####
#linear resgression
lrModel = linear_model.LinearRegression()
X = X[:, np.newaxis]
lrModel.fit(X, y)

##### task 2 #####
#logistic function
def logit(x):
    return 1 / (1 + np.exp(-x))

##### task 3 #####
#logistic regression with parameters(hypothesis)
def myModel(x, t0, t1):
    return logit(t0+x*t1)
	
#calculate values of myModel(X_test, param1, param2)
Y_test = myModel(X_test, 1, 1)

##### task 4 #####
#scikit-learn logistic regression
clf = linear_model.LogisticRegression()
clf.fit(X, y)
#Y_testLog = myModel(X_test, clf.intercept_, clf.coef_).ravel()

Y_testLog = clf.predict_proba(X_test.reshape(-1, 1))
print(Y_testLog)
Y_testLog = 1 - Y_testLog[:,0]

Y_test = clf.predict(X_test.reshape(-1, 1))

#chart
plt.figure(1, figsize=(8, 8))
plt.scatter(X.ravel(), y, color='black')

#linear
plt.plot(X_test, lrModel.coef_ * X_test + lrModel.intercept_, linewidth=1)

#logit
plt.plot(X_test, Y_test, linewidth=2)
plt.plot(X_test, Y_testLog, linewidth=2)

plt.axhline(.5, color='.5')
plt.ylabel('y')
plt.xlabel('x')
plt.xticks(range(-5, 10))
plt.yticks([0, 0.5, 1])
plt.show()