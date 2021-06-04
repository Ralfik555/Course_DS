# -*- coding: utf-8 -*-
# Link do danych: https://www.kaggle.com/c/home-data-for-ml-course
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor

# Ta opcja jest potrzebny aby wyświetlać wszyskie kolumny w takich funkcjach
# jak na describe()
pd.set_option("display.max_columns", 10)

# Ładujemy dane
melbourne_data = pd.read_csv("melb_data.csv")

# usuwamy wierwsze z brakujacymi danymi
data = melbourne_data.dropna(axis=0)

# "Price" jest tym co chcemy nauczyc sie przewidywac.
y = data.Price

# Ograniczamy liczbe feature'ow ktorych bedziemy uzywac.
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

# Tutaj tworzymy obiekt modelu "DecisionTreeRegressor", zwróćcie uwagę, że
# model ma w nazwie "Regressor". Jest to przydatna konwencja w bibliotece Sklearn
# modele dzielą się na te które mają w nazwie "Regressor" i "Classifier". Podobnie
# jak w przypadku funkcji train_test_split() używamy random_state=101 aby zawsze
# otrzymać taki sam model.
model = DecisionTreeRegressor(random_state=101)

# Słowo "fit" tak naprawdę oznacza "train". W tej linijce dzieje się cała "magia"
# czyli uczenie modelu.
model.fit(train_X, train_y)

# Obiekt "model" jest już nauczonym modelem. Tutaj wywołujemy go na "val_X" czyli
# na wektorze zmiennych wejściowych naszego walidation setu. Zmienna "preds_val"
# będzia przechowywala przewidziane ceny nieruchomości.
preds_val = model.predict(val_X)

# Obliczamy MAE korzystając z wbudowanej funkcji mean_absolute_error().
mae = mean_absolute_error(val_y, preds_val)

# Wypisujemy obliczone MAE na terminal.
print("Mean Absolute Error:  {}".format(mae))

# Zadania dla was:
# 1. Napiszcie proszę sami kod obliczającą MAE. Wynik powienien by taki
# sam wynik jak przy użyciu mean_absolute_error()
#
# 2. Korzystając z wbudowanej funkcji mean_squared_error() obliczcie RMSE.
#
# 3. Sami napiszcie kod obliczający RMSE. Wynik powienien by taki
# sam wynik jak w punkcie 2.
#
# 4. Napiszcie prosty "model" zawsze zwracający średnią cenę nieruchomości.
# Sprawdzcie jakie są wartości MAE i RMSE dla takiego modelu. Czy jest on lepszy
# niż DecisionTreeRegressor()?
#
# 5. Napiszcie prosty "model" zawsze zwracający medianę cen nieruchomości.
# Sprawdzcie jakie są wartości MAE i RMSE dla takiego modelu. Czy jest on lepszy
# niż DecisionTreeRegressor()?
