

from sklearn.cluster import KMeans
import numpy as np
from sklearn import  datasets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

iris = datasets.load_iris()

##------- wybieramy 2 pierwsze zmienne ---------
X = iris.data[:, :2]
y = iris.target

kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
kmeans.labels_
kmeans.cluster_centers_

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA','#00AAFF'])
black = ListedColormap(['#000000'])
                        
plt.figure(figsize=(14,14))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_light,s=250)
markers = ["x","*",'+']
cluser_labels = kmeans.labels_

for i, c in enumerate(np.unique(cluser_labels)):
    plt.scatter(X[:, 0][cluser_labels==c],X[:, 1][cluser_labels==c],c=cluser_labels[cluser_labels==c], marker=markers[i],cmap  = black,s=250)

plt.show()


###----------------------- Wizualizacja wielu wymiarów --------------------------------------

from sklearn.cluster import KMeans
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

boston = datasets.load_boston()
X = boston.data

##------- redukcja wymiarów PCA -------------
pca = PCA(n_components=2).fit(X)
pca_2d = pca.transform(X)

##------- redukcja wymiarów TSNE -------------
tsne_2d = TSNE(n_components=2).fit_transform(X)

##------------------ model KMEANS ---------
kmeans = KMeans(n_clusters=8, random_state=0).fit(X)
cluser_labels = kmeans.labels_

##----------- wykres PCA -----
plt.figure(figsize=(10,10))
plt.title('PCA')
plt.scatter(pca_2d[:, 0], pca_2d[:, 1], c=cluser_labels,s=250,cmap = 'Dark2')
plt.show()

#------------ wykres Tsne
plt.figure(figsize=(10,10))
plt.title('Tsne')
plt.scatter(tsne_2d[:, 0], tsne_2d[:, 1], c=cluser_labels,s=250,cmap = 'Dark2')
plt.show()

##------------------- wybór optymalnego K -------------------------

k_vec = []
int_vec = []

for k in range(2,15):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
    interia = kmeans.inertia_
    k_vec.append(k)
    int_vec.append(interia)

plt.figure(figsize=(12,10))
plt.title('Wykres sum wariancji klastów')
plt.plot(k_vec,int_vec,'bo-')
plt.xlabel('liczba klastrów')
plt.ylabel('Suma wariancji klastrów')
plt.show()


##------------- wykres dla 4 klastrów ------------------
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
cluser_labels = kmeans.labels_
plt.figure(figsize=(10,10))
plt.title('Tsne')
plt.scatter(tsne_2d[:, 0], tsne_2d[:, 1], c=cluser_labels,s=250,cmap = 'Dark2')
plt.show()

