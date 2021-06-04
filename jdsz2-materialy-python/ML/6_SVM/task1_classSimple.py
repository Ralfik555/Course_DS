from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#generate random 100 samples in two focused centers
centers = [[1, 1], [-1, -1]]
X, y = make_blobs(n_samples=80, centers=centers, random_state=0, cluster_std=0.50)
#plot data set
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plt.show()

#splitting data set into train(80%) and test(20%)

#create svm classifier, linear kernel

#fitting model to data

#predicting test

#calculating and printing accuracy
