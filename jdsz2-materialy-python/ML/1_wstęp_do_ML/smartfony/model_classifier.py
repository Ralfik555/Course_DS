# -*- coding: utf-8 -*-
# Link do danych: https://www.kaggle.com/iabhishekofficial/mobile-price-classification
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix

# Ta opcja jest potrzebny aby wyświetlać wszyskie kolumny w takich funkcjach
# jak na przykład describe().
pd.set_option("display.max_columns", 10)

# Wczytujemy dane.
dataset=pd.read_csv('train.csv')

# Przygotowujemy nasze wejście i wyjście.
X=dataset.drop('price_range',axis=1)
y=dataset['price_range']

# Wypisujemy podstawowe statystki dla naszych danych wejściowych.
print(X.describe())

# Funkcja train_test_split() w automatyczny sposób dzieli nasze dane na
# zestaw danych treningowych oraz zestaw danych walidacyjnych. Funkcja przyjmuje
# jako input "X" czyli wszystkie feature'y które są wejściem (można powiedzieć
# "wektor featerów wejściowych" oraz "y" czyli zmienną którą chcemy przewidzieć
# po angielsku "target variable" a w tym konkretnym kategoria cenowa smarfonu.
# Parametr random_state=101 jest tu po to aby za każdym razem jak wykonacie program
# podział był taki sam.
#
# Zwrócie uwagę, że wyjściem są aż 4 obiekty bo dzielimy na dwie części X i y.
train_X, val_X, train_y, val_y  = train_test_split(X, y, random_state=101)

# Tutaj tworzymy obiekt modelu "KNeighborsClassifier", zwróćcie uwagę, że
# model ma w nazwie "Classifier". Jest to przydatna konwencja w bibliotece Sklearn
# modele dzielą się na te które mają w nazwie "Regressor" i "Classifier". W przeciwieństwie
# do modelu DecisionTreeRegressor() model KNeighborsClassifier() nie używa zmiennych losowych.
# Nie ma więc potrzeby (a nawet możliwości) ustawić random_state.
model = KNeighborsClassifier(n_neighbors=20)

# Słowo "fit" tak naprawdę oznacza "train". W tej linijce dzieje się cała "magia"
# czyli uczenie modelu.
model.fit(train_X, train_y)

# Obiekt "model" jest już nauczonym modelem. Tutaj wywołujemy go na "val_X" czyli
# na wektorze zmiennych wejściowych naszego walidation setu. Zmienna "preds_val"
# będzia przechowywala przewidziane kategorie cenowe telefonów.
preds_val = model.predict(val_X)

# Używamy wbudowanej funkcji model classification_report() która oblicza wszystkie statystyki
# takie jak precision, recall oraz f1-score.
print(classification_report(val_y, preds_val))

# Używamy wbudowanej funkcji model confusion_matrix() która oblicza confusion matrix
# (https://pl.wikipedia.org/wiki/Tablica_pomyłek).
matrix = confusion_matrix(val_y, preds_val)
print(matrix)

# Zadania dla was:
# 1. Napiszcie proszę sami kod obliczającą precision, recall oraz f1-score
# classification_report().
#
# 2. Napiszcie proszę sami kod obliczającą confusion matrix wartości powinny
# być takie same jak te które uzyskacie z funkcji confusion_matrix().
