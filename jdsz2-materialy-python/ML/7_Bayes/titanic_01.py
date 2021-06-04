# -*- coding: utf-8 -*-
# Link do Kaggle: https://www.kaggle.com/c/titanic/data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


# Ustawiamy liczbę wyświetlanych kolumn dla DataFrame
pd.set_option("display.max_columns", 12)

# Ładujemy dane przy pomocy funkcji wbudowanej w bibliotekę pandas
train_df = pd.read_csv("train.csv")

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

# Tworzymy model GaussianNB()
clf_gnb = GaussianNB()

# Tworzymy model DecisionTreeClassifier()
clf_dt = DecisionTreeClassifier(random_state=0)

# Trenujemy model GaussianNB na danych treningowych
clf_gnb.fit(X_train,y_train)

# Trenujemy model DecisionTreeClassifier na danych treningowych
clf_dt.fit(X_train,y_train)

# Dokonujemy predykcji dla danych testowych przy użyciu GaussianNB
y_pred_gnb = clf_gnb.predict(X_test)

# Dokonujemy predykcji dla danych testowych przy użyciu DecisionTreeClassifier
y_pred_dt = clf_dt.predict(X_test)


# Obliczamy dokładność dla danych testowych dla GaussianNB
score_gnb = accuracy_score(y_test, y_pred_gnb)

# Obliczamy dokładność dla danych testowych dla DecisionTreeClassifier
score_dt = accuracy_score(y_test, y_pred_dt)

print("Accuracy dla GaussianNB {} a dla DecisionTreeClassifier {}".format(score_gnb, score_dt))

# Praca domowa:
# W katalogu "7_Bayes" znajduje się plik "test.csv". Jest to plik bardzo podobny w strukturze do
# "train.csv" ale nie zawiera naszego "target variable" czyli informacji o tym kto
# przeżył a kto nie. Plik "test.csv został przygotowany przez twórców konkursu i zawiera informacje
# o pasażerach którzy nie występują w pliku "train.csv". Należy dokonać predykcji dla wszystkich
# wierszy i stworzyć plik z rezultatem o strukturze podobnej do pliku "gender_submission.csv". W pliku
# "gender_submission.csv" zakładamy prosty model: każda  każda kobieta przeżyła a każdy mężczyzna nie.
# Oczywiście my chcemy użyć  modelu który wytrenowaliśmy. Bazuje on na dużo większej liczbie featere'ów
# i liczymy na lepszy wyniki niż prosty model oparty o płeć.
#
# Zadanie polega więc na stworzeniu pliku analogicznego do "gender_submission.csv" ale zawierającego predykcję
# z naszych modeli. Uzyskany plik wyślijcie jako na stronie Kaggle i pochwalcie się na Slacku jaki macie wynik.