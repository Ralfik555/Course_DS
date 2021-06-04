import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_circles
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#create data grouped in circles
X, y = make_circles(100, factor=.1, noise=.1)

#create main figure
fig = plt.figure()

#add subplot to the figure 2-number of rows, 1-number of columns, 1-idx number of subplot
flatFig = fig.add_subplot(211)

#put data into plot
flatFig.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')

#set title of the plot
flatFig.set_title("raw data")

#polynomial kernel
#z = np.power((X[:, 0] + X[:, 1] + 3), 3)

#rbf, gaussian
gamma2 = 1
z = np.exp(-(X ** 2).sum(1)/gamma2)

#expanding dimensions to get same number as X
z = np.expand_dims(z, 1)

#concatenating X and z to get extended feature table
Xext = np.concatenate((X, z), 1)
print("shape of Xext: ", Xext.shape)

#creating subplot below previous one, 3d projection type
threeDFig = fig.add_subplot(212, projection='3d')

#put data into plot
threeDFig.scatter3D(Xext[:, 0], Xext[:, 1], Xext[:, 2], c=y, s=50, cmap='autumn')

#set axis and title names
threeDFig.set_xlabel('x')
threeDFig.set_ylabel('y')
threeDFig.set_zlabel('z')
threeDFig.set_title("data after dimension extended, 3d")

#finally show plot
plt.show()
