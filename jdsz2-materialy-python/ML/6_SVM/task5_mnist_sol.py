# importing necessary libraries
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np

# loading the digits dataset
digits = datasets.load_digits()

print("digits.data.shape: ", digits.data.shape)
print("digits.target.shape: ", digits.target.shape)
plt.gray()
plt.matshow(digits.images[100])
plt.show()

# X -> features, y -> label
X = digits.data
y = digits.target

# dividing X, y into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# training a linear SVM classifier
clf = svm.SVC(kernel='linear', C=1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# model accuracy for X_test
accuracy = clf.score(X_test, y_test)
print("accuracy: ", accuracy)

# creating a confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("cm:\n", cm)
