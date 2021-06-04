import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

#input data
X = np.arange(-5.0,10.0,0.2)
y = (X > 2).astype(np.float)

#test data
X_test = np.linspace(-10, 10, 300)

#input data chart
plt.figure(1, figsize=(8, 8))
plt.scatter(X, y, color='blue')
plt.ylabel('y')
plt.xlabel('X')
plt.xticks(range(-5, 10))
plt.yticks([0, 0.5, 1])
plt.show()

##### task 1 #####
#linear resgression

#linear refression

##### task 2 #####
#logistic function
	
#values of logit(X_test)

#results chart

##### task 3 #####
#logistic regression with parameters(hypothesis)
	
#calculate values of myModel(X_test, param1, param2)

#chart

##### task 4 #####
#scikit-learn logistic regression

#chart