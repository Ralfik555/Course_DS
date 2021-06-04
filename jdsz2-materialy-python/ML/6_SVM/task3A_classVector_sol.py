import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_circles
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mlxtend.plotting import plot_decision_regions

#create data grouped in circles
#X, y = make_circles(100, factor=.1, noise=.1)
X = np.linspace(-5,5,20)
y = np.zeros(len(X), np.int)
y[:7] = 1
y[12:] = 1

#create main figure
fig = plt.figure()

#add subplot to the figure 2-number of rows, 1-number of columns, 1-idx number of subplot
flatFig = fig.add_subplot(211)

#put data into plot
flatFig.scatter(X, X, c=y, s=50, cmap='autumn')

#set title of the plot
flatFig.set_title("raw data")

#new feature
xtmp = X**2
#expanding dimensions to get same number as X
X = np.expand_dims(X, 1)
xtmp = np.expand_dims(xtmp, 1)

#concatenating X and r to get extended feature table
Xext = np.concatenate((X, xtmp), 1)
print("shape of Xext: ", Xext.shape)

#add subplot to the figure 2-number of rows, 1-number of columns, 1-idx number of subplot
flatFig = fig.add_subplot(212)

#put data into plot
flatFig.scatter(Xext[:,0], Xext[:,1], c=y, s=50, cmap='autumn')

#set title of the plot
flatFig.set_title("row data, 2d plot")
plt.show()

#splitting data set into train and test
X_train, X_test, y_train, y_test = train_test_split(Xext, y, test_size=0.1, random_state=42)

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
plot_decision_regions(X=Xext, y=y, clf=clf, legend=2)

plt.show()
