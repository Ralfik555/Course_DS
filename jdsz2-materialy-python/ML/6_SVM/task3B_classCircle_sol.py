import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_circles
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#create data grouped in circles
X, y = make_circles(100, factor=.4, noise=.2)

#create main figure
fig = plt.figure()

#add subplot to the figure 2-number of rows, 1-number of columns, 1-idx number of subplot
flatFig = fig.add_subplot(211)

#put data into plot
flatFig.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')

#set title of the plot
flatFig.set_title("row data, 2d plot")

#polynomial kernel
#z = np.power((X[:, 0] + X[:, 1] + 3), 3)

#rbf, gaussian
gamma2 = 1
z = np.exp(-(X ** 2).sum(1)/gamma2)

#expanding dimensions to get same number as X
z = np.expand_dims(z, 1)

#concatenating X and r to get extended feature table
Xext = np.concatenate((X, z), 1)
print("shape of Xext: ", Xext.shape)

#creating subplot below previous one, 3d projection type
threeDFig = fig.add_subplot(212, projection='3d')

#put data into plot
threeDFig.scatter3D(Xext[:, 0], Xext[:, 1], Xext[:, 2], c=y, s=50, cmap='autumn')

#set axis and title names
threeDFig.set_xlabel('x')
threeDFig.set_ylabel('y')
threeDFig.set_zlabel('r')
threeDFig.set_title("data after dimension extended, 3d")

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

#generating tmp data for hyperplane
tmp = np.linspace(-1, 1, 21)
xSpace, ySpace = np.meshgrid(tmp, tmp)

print("clf.coef_: ", clf.coef_)
print("clf.intercept_: ", clf.intercept_)

#plane equation a*x+b*y+c*z+d=0
#z should be calculated
zSpace = (-clf.intercept_[0]-clf.coef_[0][0]*xSpace-clf.coef_[0][1]*ySpace) / clf.coef_[0][2]

#plot hyperplane
threeDFig.plot_surface(xSpace, ySpace, zSpace)

#finally show plot
plt.show()
