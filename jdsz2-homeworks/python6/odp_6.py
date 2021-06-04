   
#######################################################################################################
######################------------- ZADANIE 1 ----------------#########################################
#######################################################################################################


from sklearn.neighbors import BallTree
import pickle
from sklearn import neighbors, datasets
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn import preprocessing

data = fetch_california_housing()
df = pd.DataFrame(data.data,columns = data.feature_names)


##----------- podział na zbiór testowy i wlidacyjny -----------
train_X, val_X  = train_test_split(df,  random_state=101,test_size =0.3)

##----------- wyliczenie parametrów do normaliacji i normalizacja zbioru treningowego --------------
quarties = np.array(train_X[['Population']].quantile([0.25,0.75]))
down = float(quarties[0]  - 1.5 * quarties[1]-quarties[0] )
up = float(quarties[1]  + 1.5 * quarties[1]-quarties[0] )

df_ro = train_X.loc[(train_X['Population'] > down) & (df['Population'] < up)]
norm_scale = preprocessing.StandardScaler().fit(df_ro[['Population', 'HouseAge']])
df_norm_ro = norm_scale.transform(df_ro[['Population', 'HouseAge']])

### ------ wyliczenie sd i mean oraz wrzucenie do słownika ----
zm = ['Population','HouseAge']
stat_dict = {}

for z in zm:
    stat_dict[z] = {'mean':np.mean(df_ro[z]),'sd': np.std(df_ro[z])}

    
##------------ utworzenie obiektu drzewa -----
tree = BallTree(df_norm_ro, leaf_size=40,metric ='euclidean' ) 

###---------- zapiklowanie i otworzenie pikla -------
model_obj = {'model':tree,'norm_stats':stat_dict }

with open('model.pickle', 'wb') as f:
    pickle.dump(model_obj, f)

with open('model.pickle', 'rb') as f:
    loaded_model = pickle.load(f)

###--------- wczytanie modelu z pikla ---
loaded_tree = loaded_model['model']

###----------- utworzenie znormalizywoonaych danych na podstawie parametrów ---
val_norm = pd.DataFrame()
for z in loaded_model['norm_stats']:
    val_norm[z] = (val_X[z]- loaded_model['norm_stats'][z]['mean'])/ loaded_model['norm_stats'][z]['sd']   

##----- reset indexów ----------
val_norm.index = range(len(val_norm))

##----------- wyliczenie K nijblizszych sonsiadów ----
dist, ind = loaded_tree.query(val_norm[:1]  , k=5)  
print(ind)
1
   
#######################################################################################################
######################------------- ZADANIE 2 ----------------#########################################
#######################################################################################################


###------------------- Z ZAJĘĆ Z KUBĄ ----------------------------------------------------------

import numpy as np
import pandas as pd

# Wczytujemy plik "weatherAUS.csv" przy użyciu bilioteki pandas
df = pd.read_csv('weatherAUS.csv')
# Wypisujemy wymiary wczytanego pliku
#print('Wymiary wczytanego pliku:',df.shape)

# Wypisujemy pierwsze 5 wierszy DataFrame.
df[0:5]

# Sprawdźmy które kolumny mają dużo "missing values".
# Żeby dobrze zrozumieć co się dzieje w tej linijce warto wypisać sobie poszczególne
# wartości oddzielnie, czyli:
# df.isnull()
# df.isnull().sum()
df.isnull().sum().sort_values()

# Usuwamy 4 kolumny które mają mniej niż 60 % danych
# Usuwamy też, "location", bo chcemy aby nasz model przewidywał
# dane nizależnie dla całej Australii
# Usuwamy RISK_MM poniważ jest to ściśle powiązane z 'RainTomorrow'
# Na stronie https://www.kaggle.com/jsphyg/weather-dataset-rattle-package możemy przeczytać definicję RISK_MM:
# RISK_MM - The amount of rain. A kind of measure of the "risk".
df = df.drop(columns=['Sunshine','Evaporation','Cloud3pm','Cloud9am','Location','RISK_MM','Date'],axis=1)

# Wypisujemy wymiary "df" po usunięciu 7 kolumn, z 24 zostało ich 17
df.shape

# Usuwamy wszystkie NaN (not a number)
df = df.dropna(how='any')
# Wypisujemy wymiary "df" po usunięciu NaN z 142193 wierszy zostało 112925
df.shape

# Zamieniamy "Yes" i "no" na wartości liczbowe
df['RainToday'].replace({'No': 0, 'Yes': 1},inplace = True)
df['RainTomorrow'].replace({'No': 0, 'Yes': 1},inplace = True)

# Zamiana kategorycznych wartości przy użyciu pd.getDummies()
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html
categorical_columns = ['WindGustDir', 'WindDir3pm', 'WindDir9am']
for col in categorical_columns:
    print(np.unique(df[col]))
df = pd.get_dummies(df, columns=categorical_columns)

# Wypisujemy pierwsze 5 wierszy DataFrame. Zwróćmy uwagę na kolumny:
# "WindDir9am_NNW", "WindDir9am_NW", "WindDir9am_S" etc...
# jest to efekt działania funkcji get_dummies(), zamienia ona "stringi" czyli napisy na
# wartości liczbowe. Więcej na:
# https://hackernoon.com/what-is-one-hot-encoding-why-and-when-do-you-have-to-use-it-e3c6186d008f
df.iloc[0:5]


from sklearn import preprocessing

# W tej linijce tylko tworzymy MinMaxScaler()
scaler = preprocessing.MinMaxScaler()

# Tutaj przekazujemy do Scalera nasze dane i scaler analizuje wszystkie wartości
scaler.fit(df)

# W tej lini następuje faktyczne przekształcenie danych.
df = pd.DataFrame(scaler.transform(df), index=df.index, columns=df.columns)


X = df.loc[:,df.columns!='RainTomorrow']
y = df[['RainTomorrow']]


from sklearn.model_selection import train_test_split
# Dzielimy dane na train i test set (75% to train set, zaś 25% to test set).
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
print(X_train.shape)
print(X_test.shape)


#Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time
#Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


################---------------------- WŁACIWA PRACA DOMOWA ------------------------------------------

##-------- model bazowy-------------
clf_rf = RandomForestClassifier(n_estimators=10, max_depth=10,random_state=0, min_samples_leaf=2, criterion="gini")
clf_rf.fit(X_train, y_train)
y_pred = clf_rf.predict(X_test)
score = accuracy_score(y_test, y_pred)


###------------------ to jest przykład jak można podeć do znalezienia najlepszych hyperparametrów--
###------------------ można podchodzić do tego bardzo różnie, nie należy też robić zbyt wiele kombinacji
###------------------ bo stracimy bardzo dużo czasu a uzysk będzie raczej nieduży, należy najpierw --
##------------------- zastanowić się jakie parametry mogą wpłynać na skutecznosć  ---------


es_score = []
for es in range(10,200,20):
    
    clf_rf = RandomForestClassifier(n_estimators=es, max_depth=None, min_samples_split=2, random_state=0,
                                min_samples_leaf=2, criterion="gini")
    
    clf_rf.fit(X_train, y_train)
    y_pred = clf_rf.predict(X_test)
    es_score.append(accuracy_score(y_test, y_pred))

###--------- widać na wykresie że róznice mamy do 50, powyżej uzysk nie jest już duży ---
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.plot(list(range(10,200,20)),es_score)
plt.show()

##------------- najlepszy n_estitators -------------
best_es = list(range(10,200,20))[np.argmax(es_score)]

mf_score = []
for mf in range(10,60,5):
    
    ##------- tutaj damy 50, bo im więcej n_estimators tym liczy się dłużej, a na wykresie powyżej
    ##------- widzimy że powyżej 50 niewiele nam się poprawia skutecznoc -------------------------
    clf_rf = RandomForestClassifier(n_estimators=50, max_depth=None, min_samples_split=2, random_state=0,
                                min_samples_leaf=2, criterion="gini", max_features = mf)
    
    clf_rf.fit(X_train, y_train)
    y_pred = clf_rf.predict(X_test)
    mf_score.append(accuracy_score(y_test, y_pred))

plt.figure(figsize=(10,10))
plt.plot(list(range(10,60,5)),mf_score)
plt.show()

###------------- tutaj mam największą skutecznosc gdy bierzemy wszystkie zmienne, czasem może sie zdarzyc
####------------- ze częsc zmiennych powoduje nam szumy, wiec warto sprawdzic max_features ----------


mf_score = []
for mf in range(10,60,5):
    
    ##------- tutaj damy 50, bo im więcej n_estimators tym liczy się dłużej, a na wykresie powyżej
    ##------- widzimy że powyżej 50 niewiele nam się poprawia skutecznoc -------------------------
    clf_rf = RandomForestClassifier(n_estimators=50, max_depth=None, min_samples_split=2, random_state=0,
                                min_samples_leaf=2, criterion="gini", max_features = mf)
    
    clf_rf.fit(X_train, y_train)
    y_pred = clf_rf.predict(X_test)
    mf_score.append(accuracy_score(y_test, y_pred))


msl_score = []
for msl in [2,5,10,20,50]:
    
    ##------- tutaj damy 50, bo im więcej n_estimators tym liczy się dłużej, a na wykresie powyżej
    ##------- widzimy że powyżej 50 niewiele nam się poprawia skutecznoc -------------------------
    clf_rf = RandomForestClassifier(n_estimators=50, max_depth=None, min_samples_split=2, random_state=0,
                                min_samples_leaf = msl, criterion="gini", max_features = mf)
    
    clf_rf.fit(X_train, y_train)
    y_pred = clf_rf.predict(X_test)
    msl_score.append(accuracy_score(y_test, y_pred))

plt.figure(figsize=(10,10))
plt.plot([2,5,10,20,50],msl_score)
plt.show()

clf_rf = RandomForestClassifier(n_estimators=150, max_depth=None, min_samples_split=2, random_state=0,
                                min_samples_leaf=2, criterion="gini")
    
clf_rf.fit(X_train, y_train)
y_pred = clf_rf.predict(X_test)
final_score = accuracy_score(y_test, y_pred)


