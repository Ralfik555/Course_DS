# importing necessary libraries
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np


def make_meshgrid(x, y, h=.02):
    """Create a mesh of points to plot in

    Parameters
    ----------
    x: data to base x-axis meshgrid on
    y: data to base y-axis meshgrid on
    h: stepsize for meshgrid, optional

    Returns
    -------
    xx, yy : ndarray
    """
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy


def plot_contours(ax, clf, xx, yy, **params):
    """Plot the decision boundaries for a classifier.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional
    """
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out


# loading the iris dataset
dataSet = datasets.load_iris()
#dataSet = datasets.load_breast_cancer()
#dataSet = datasets.load_digits()

# X -> features, y -> label
X = dataSet.data[:, :2]
y = dataSet.target

print("X.shape", X.shape)
print("y.shape", y.shape)

# dividing X, y into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.5,)

# training a linear SVM classifier
clf = svm.SVC(kernel='linear', C=1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

#logistic regression model
clfL = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
clfL.fit(X_train, y_train)
y_predL = clfL.predict(X_test)

# model accuracy for X_test
accuracy = clf.score(X_test, y_test)
print("accuracy: ", accuracy)

# modelL accuracy for X_test
accuracyLogistic = clfL.score(X_test, y_test)
print("accuracyLogistic: ", accuracyLogistic)

# # Plot Decision Region using mlxtend's
# #plot_decision_regions(X=X, y=y, clf=clf, legend=2)
# X0, X1 = X[:, 0], X[:, 1]
# xx, yy = make_meshgrid(X0, X1)
#
# fig = plt.figure()
# subFig = fig.add_subplot(111)
# plot_contours(subFig, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
# subFig.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
#
# plt.show()

# creating a confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("cm:\n", cm)

cmL = confusion_matrix(y_test, y_predL)
print("cmL:\n", cmL)
