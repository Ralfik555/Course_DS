import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mlxtend.plotting import plot_decision_regions

plt.figure()
plt.title("Three classes, two features, one cluster", fontsize='small')
X, y = make_classification(n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1, n_classes=3)
plt.scatter(X[:, 0], X[:, 1], marker='o', c=y, s=25, edgecolor='k')
plt.show()

#splitting data set into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#create svm classifier, linear kernel
clfStandard = svm.SVC(kernel='linear')
clf = OneVsRestClassifier(svm.SVC(kernel='linear'))

#fitting model to data
clfStandard.fit(X_train, y_train)
clf.fit(X_train, y_train)

#predicting test
yStandard_pred = clfStandard.predict(X_test)
y_pred = clf.predict(X_test)

#calculating accuracy
accStandard = accuracy_score(y_test, yStandard_pred)
acc = accuracy_score(y_test, y_pred)
print("accStandard: ", accStandard)
print("acc: ", acc)

# Plot Decision Region using mlxtend's
plot_decision_regions(X=X, y=y, clf=clfStandard, legend=2)
plt.show()
plot_decision_regions(X=X, y=y, clf=clf, legend=2)
plt.show()