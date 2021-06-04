# -*- coding: utf-8 -*-
# Link do danych: https://www.kaggle.com/c/home-data-for-ml-course
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Ta opcja jest potrzebny aby wyświetlać wszyskie kolumny w takich funkcjach
# jak na przykład describe().
pd.set_option("display.max_columns", 10)

# Ładujemy dane.
melbourne_data = pd.read_csv("melb_data.csv")

# Usuwamy wierwsze z brakujacymi danymi.
data = melbourne_data.dropna(axis=0)

# "Price" jest tym co chcemy nauczyc sie przewidywac.
y = data.Price

# Ograniczamy liczbe feature'ow ktorych bedziemy używać.
feature_list = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea',
                      'YearBuilt', 'Lattitude', 'Longtitude']
X = data[feature_list]

# Wypisujemy podstawowe statystki dla naszych danych wejściowych.
print(X.describe())

# Funkcja train_test_split() w automatyczny sposób dzieli nasze dane na
# zestaw danych treningowych oraz zestaw danych walidacyjnych. Funkcja przyjmuje
# jako input "X" czyli wszystkie feature'y które są wejściem (można powiedzieć
# "wektor featerów wejściowych" oraz "y" czyli zmienną którą chcemy przewidzieć
# po angielsku "target variable" a w tym konkretnym przypadku ceny nieruchomości.
# Parametr random_state=101 jest tu po to aby za każdym razem jak wykonacie program
# podział był taki sam.
#
# Zwrócie uwagę, że wyjściem są aż 4 obiekty bo dzielimy na dwie części X i y.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=101)

# W pętli iterujemy od 1 do 7. Za każdym razem trenujemy model DecisionTreeRegressor()
# z inną wartością max_features. Parametr max_features to maksymalna liczba featerów które
# model drzewa decyzyjnego może użyć aby dokonać podziału drzewa (więcej dokładnego info na
# ten temat będzie podczas zajęć dotyczących drzew decyzyjnych).
#
# Intuicyjnie możemy założyć, że większe max_features oznacza bardziej skomplikowany model.
# Przykładowo dla max_features=1 model może podjąć decyzję: jeżeli liczba łazienek jest
# większa niż 1 to ... Ale zabraniamy mu brać pod uwagę jednocześnie liczbę łazienek i rok
# budowy. Problem z bardziej skomplikowanym modelem jest taki, że może on overfitować (po polsku:
# "może wystąpić problem nadmiernego dopasowania"). Dlatego dla wszystkich możliwych wartości
# max_features obliczamy wartość MAE dla zestawu danych walidacyjnych.
for max_features in [1, 2, 3, 4, 5, 6, 7]:
    # Tutaj tworzymy nasz model i ustawiamy max_features.
    model = DecisionTreeRegressor(max_features=max_features, random_state=101)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    print("Max features: {}    Mean Absolute Error:  {}".format(max_features, mae))
