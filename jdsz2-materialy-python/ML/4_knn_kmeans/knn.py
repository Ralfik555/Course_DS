
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
 
##----------------
iris = datasets.load_iris()

##------- wybieramy 2 pierwsze zmienne ---------
X = iris.data[:, :2]
y = iris.target
## ---------------- definicje kolorów (hex) ------
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA','#00AAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00','#004D99'])
                            
###------------ budowa klasyfikatora knn ---------------------------------
n_neighbors = 6
clf = neighbors.KNeighborsClassifier(n_neighbors, weights='uniform')
clf.fit(X, y)
 
###-------------- budowa siatki dla wykresu ------------------
h = .02
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

##-----------  predykcja dla całej siatki --------
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
##---- predykcja zwraca array, tutaj dostosowujemy kształt do siatki ---- 
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10,10))
###------- kolorujemy przestrzen na podstawie siatki ---------
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
##--------- nanosimy punkty -----------------
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,edgecolors='black')
plt.title("3-Class classification (k = {0})".format( n_neighbors))
plt.show()











