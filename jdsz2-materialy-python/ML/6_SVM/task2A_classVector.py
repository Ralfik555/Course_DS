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

##### PART A #####

#new feature

#expanding dimensions to get same number as X

#concatenating X and r to get extended feature table

#add subplot to the figure 2-number of rows, 1-number of columns, 1-idx number of subplot

#put data into plot

#set title of the plot

plt.show()

##### PART B #####

#splitting data set into train and test

#create svm classifier, linear kernel

#fitting model to data

#predicting test

#calculating accuracy

# Plot Decision Region using mlxtend's
#plot_decision_regions(X=Xext, y=y, clf=clf, legend=2)

plt.show()
