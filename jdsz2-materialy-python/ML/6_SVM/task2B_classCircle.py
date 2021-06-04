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
flatFig = fig.add_subplot(111)

#put data into plot
flatFig.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')

#set title of the plot
flatFig.set_title("raw data")

##### PART A #####

#polynomial kernel

#rbf, gaussian

#expanding dimensions to get same number as X

#concatenating X and z to get extended feature table

#creating subplot below previous one, 3d projection type
#threeDFig = fig.add_subplot(212, projection='3d')

#put data into plot
#threeDFig.scatter3D(?, ?, ?, c=y, s=50, cmap='autumn')

#set axis and title names
#threeDFig.set_xlabel('x')
#threeDFig.set_ylabel('y')
#threeDFig.set_zlabel('z')
#threeDFig.set_title("data after dimensions extended, 3d")

##### PART B #####

#splitting data set into train and test

#create svm classifier, linear kernel

#fitting model to data

#predicting test

#calculating accuracy

#plot model decision boundary

plt.show()
