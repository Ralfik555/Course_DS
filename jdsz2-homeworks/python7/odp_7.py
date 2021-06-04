
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
from sklearn.multiclass import OneVsRestClassifier

digits = datasets.load_digits()

X = digits.data 
Y = digits.target
##---------- podział na zbiór uczący i walidacyjny oraz nauczenie modelu ----------------
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0,train_size = 0.7)
clf = OneVsRestClassifier(svm.SVC(kernel='linear', C=5))
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

#####--------- redukcja wymiarów tsne ----------
tsne_2d = TSNE(n_components=2).fit_transform(X_test)

###--- cyfry (klasy Y) -----------
factors = list(set(y_test))

plt.figure(figsize=(12,12))
##------- w pętli rysujemy kolejne wykresy dla poszczególnych cyfr, ponadto dodajemy etykiety dla legendy------
for f in factors:
    plt.scatter(tsne_2d[:,0][y_test==f],tsne_2d[:,1][y_test==f],label=str(f), s=80,edgecolors='k')
##------ rysujemy legende w optymalnym miejscu
plt.legend(loc='upper best')
####--------- rysujemy te punty, które svm źle sklasyfikował --------------
plt.scatter(tsne_2d[:,0][y_test!=y_pred],tsne_2d[:,1][y_test!=y_pred], s=200, marker='x',c  = 'k')
plt.show()

