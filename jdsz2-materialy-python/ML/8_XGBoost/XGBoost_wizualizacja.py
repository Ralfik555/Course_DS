# -*- coding: utf-8 -*-
# Link do Kaggle: https://www.kaggle.com/c/titanic/data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from xgboost import plot_tree
import matplotlib.pyplot as plt

# Ustawiamy liczbę wyświetlanych kolumn dla DataFrame
pd.set_option("display.max_columns", 12)

# Ładujemy dane przy pomocy funkcji wbudowanej w bibliotekę pandas
train_df = pd.read_csv("../7_Bayes/train.csv")

# Wypisujemy pierwsze 5 wierszy
print(train_df.head())

# Tworzymy nasze "target variable" czyli to co chcemy przewidywać.
# W tym przypadku jest to kolumna "Survived" zawierająca "1" jeżeli
# dana osoba przeżyła katastrofę i "0" w przeciwnym wypadku.
target = train_df["Survived"]

# Lista kolumn które chcemy usunąć.
columns_to_delete = ["Name", "Survived", "PassengerId", "Ticket"]

# Lista kolumn z wartościami które poddamy "dummifikacji"
# Więcej można przeczytać na:
# https://hackernoon.com/what-is-one-hot-encoding-why-and-when-do-you-have-to-use-it-e3c6186d008f
categorical_columns = ["Sex", "Cabin", "Pclass", "Embarked",]

# Usuwamy kolumny wcześniej zdefiniowane w liście columns_to_delete
train_df = train_df.drop(columns=columns_to_delete ,axis=1)

# Zamieniamy feature'y ketegoryczne na reprezentacje liczbową
train_df = pd.get_dummies(train_df, columns=categorical_columns)

# Używając funkcji isnull() na naszym DataFrame "train_df" sprawdzamy
# czy któreś kolumny mają wartości NaN (Not a Number)
print(train_df.isnull().any())
print("----------------")

# Używamy funkcji "fillna()" aby zamienić NaN dla kolumny "Age" na
# średnią wartość dla wszystkich ludzi. Zwróćcie uwagę na użycie
# inplace=True, bez tego ta linijka musiałaby wyglądać tak:
# train_df["Age"] = train_df["Age"].fillna(value = train_df["Age"].mean())
train_df["Age"].fillna(value = train_df["Age"].mean(), inplace=True)

# Używając raz jeszcze funkcji isnull() sprawdzamy czy poprawnie
# pozbyliśmy się NaN z kolumny "Age"
print(train_df.isnull().any())

# Sprawdźmy jak wyglądają dane po wszystkich transformacjach
print(train_df.head())

# Dzielimy dane na train i test set (75% to train set, zaś 25% to test set),
# random_state użwamy tutaj po to abyście odpalając skrypt zawsze mieli taki sam podział.
X_train, X_test, y_train, y_test = train_test_split(train_df, target, test_size=0.25, random_state=11)


# Tworzymy model XGBClassifier z 10 drzewami i maksymalną głębokości każdego
# z nich równą 3
clf_xgbc = XGBClassifier(n_estimators=10, max_depth=3,)

# Uczymy model XGBClassifier
clf_xgbc.fit(X_train, y_train)

# Dokonujemy predykcji dla danych testowych przy użyciu XGBClassifier
y_pred_xgb = clf_xgbc.predict(X_test)

# Obliczamy dokładność dla danych testowych dla XGBClassifier
score_xgb = accuracy_score(y_test, y_pred_xgb)
print("score_xgb {}".format(score_xgb))

# Wizualizacja pierwszego drzewa naszego modelu
plot_tree(clf_xgbc, num_trees=0)

plt.show()
