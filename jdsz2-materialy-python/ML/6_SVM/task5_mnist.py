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
