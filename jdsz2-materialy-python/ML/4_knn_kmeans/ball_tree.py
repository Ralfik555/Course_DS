
from sklearn.neighbors import BallTree
import pickle
from sklearn import neighbors, datasets
 

data = datasets.load_breast_cancer()
X = data.data[:, :2]
y = data.target

###----------- tworzymy obiekt drzewa knn (ball tree) ---------------------------------------------
##-------- bez pierwszej obserwacji, bo dla niej będziemy sprawdzać jakie obserwacje leżą najbliżej

tree = BallTree(X[1:], leaf_size=40,metric ='euclidean' ) 
## --- można użyć też powołując się na klasę metryki np
tree = BallTree(X[1:], leaf_size=40,metric =neighbors.dist_metrics.MinkowskiDistance(2)) 

###-------- odległosci i indexy k najblizszch obserwacji, dla obserwacji z X o indexie 0 ---
##--------- do query w tym przypadku potrzebujemy macieży o 2 kolumnach, więc nadajemy odpowiedni kształt dla obserwacji X[0] 
dist, ind = tree.query(X[0].reshape(1,2), k=3)     

#---- odległosc od k najblizszych obserwacji
print('odległosc od k najblizszych obserwacji \n',dist,'\n')
##--- indeksy k najblizszych obserwacji 
print('indeksy k najblizszych obserwacji  \n',ind,'\n')

##----- piklowanie obiektu i wczytywanie -----------

model_obj = {'model':tree,'opis':'Ball Tree dla zbioru iris' }
print(model_obj)

with open('model.pickle', 'wb') as f:
    pickle.dump(model_obj, f)

with open('model.pickle', 'rb') as f:
    loaded_model = pickle.load(f)

loaded_tree = loaded_model['model']
dist, ind = loaded_tree.query(X[0].reshape(1,2), k=3)  

#---- odległosc od k najblizszych obserwacji
print('odległosc od k najblizszych obserwacji \n',dist,'\n')
##--- indeksy k najblizszych obserwacji 
print('indeksy k najblizszych obserwacji  \n',ind,'\n')


###----  Zadanie 2 KNN ----------------------
###----  symulacja produkcyjnej sytuacji ----
##-----  zbiór california_hausing podzielić na treningowy i testowy i zbiór testowy ustandaryzować jak w zadaniu ze standaryzacja
##------ zapisać parametry mean i sd, które posłużyły do standaryzacji a następnie utworzyć ball tree na zbiorze treningowym
###----- zapiklować słownik z ball tree oraz z parametrami sd i mean.
#------- nastepnie, kożystając z tego pickla wypisać 5 najbliższych sąsiadów dla dowolnej obserwacji ze zbioru testowego.
