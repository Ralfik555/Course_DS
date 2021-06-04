from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def plot_svc_decision_function(model, ax=None, plot_support=True):
    """Plot the decision function for a 2D SVC"""
    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # create grid to evaluate model
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)

    # plot decision boundary and margins
    ax.contour(X, Y, P, colors='k',
               levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])

    # plot support vectors
    if plot_support:
        ax.scatter(model.support_vectors_[:, 0],
                   model.support_vectors_[:, 1],
                   marker='x',
                   linewidths=1,
                   s=100
                   )
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)


#generate random 100 samples in two focused centers
centers = [[1, 1], [-1, -1]]
X, y = make_blobs(n_samples=80, centers=centers, random_state=0, cluster_std=0.50)
#plot data set
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')

#splitting data set into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#create svm classifier, linear kernel
clf = svm.SVC(kernel='linear')

#fitting model to data
clf.fit(X_train, y_train)

#predicting test
y_pred = clf.predict(X_test)

#calculating accuracy
acc = accuracy_score(y_test, y_pred)
print("acc: ", acc)

#plot model decision boundary
plot_svc_decision_function(clf, plot_support=True)
plt.show()

print("support vectors")
print(clf.support_vectors_)
