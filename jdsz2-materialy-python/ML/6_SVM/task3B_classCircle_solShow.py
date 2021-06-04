import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_circles
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mlxtend.plotting import plot_decision_regions

#create data grouped in circles
X, y = make_circles(100, factor=.1, noise=.1)

#create main figure
fig = plt.figure()

#add subplot to the figure 2-number of rows, 1-number of columns, 1-idx number of subplot
flatFig = fig.add_subplot(111)

#put data into plot
flatFig.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')

#set title of the plot
flatFig.set_title("raw data, 2d")

#splitting data set into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

#create svm classifier, linear kernel
clf = svm.SVC(kernel='linear')

#fitting model to data
clf.fit(X_train, y_train)

#predicting test
y_pred = clf.predict(X_test)

#calculating accuracy
acc = accuracy_score(y_test, y_pred)
print("acc: ", acc)

# Plot Decision Region using mlxtend's
plot_decision_regions(X=X, y=y, clf=clf, legend=2)

#finally show plot
plt.show()
