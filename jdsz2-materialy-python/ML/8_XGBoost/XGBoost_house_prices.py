import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer
from sklearn.metrics import mean_squere_error

# Wczytujemy dane treningowe
data = pd.read_csv('train.csv')

# Wczytujemy dane testowe używane na kagglowym leaderboard
test_kaggle = pd.read_csv("test.csv")

# Tworzymy "target variable"
y = data["SalePrice"]

# Usuwamy "target variable" z X, jednocześnie pozbywamy się wszystkich
# kolumn które mają typ danych == "object". Jest to dosyć "agresywne"
# podejście które pozostawia tylko nieproblematyczne feature'y.
X = data.drop(["SalePrice"], axis=1).select_dtypes(exclude=["object"])

# Tą samą operację usunięcia problematycznych featere'ów powtarzamy dla
# danych testowych.
test_kaggle_X = test_kaggle.select_dtypes(exclude=['object'])


# Dzielimy dane treningowe na train i test set (inną odpowiednią nazwą jest tutaj
# "dane walidacyjne" ang. "validation data").
# Random_state użwamy tutaj po to abyście odpalając skrypt zawsze mieli taki sam podział.
X_train, X_test, y_train, y_test = train_test_split(X.as_matrix(), y.as_matrix(), test_size=0.25, random_state=11)

# Prosty i automatyczny sposób na pozbycie się brakujących wartości dla featureów
# https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html
my_imputer = Imputer()
my_imputer.fit(X)
train_X = my_imputer.transform(X_train)
test_X = my_imputer.transform(X_test)
test_kaggle_X = my_imputer.transform(test_kaggle_X)

# Tworzymy model XGBRegressor()
clf_xgbr = XGBRegressor()

# W tej lini następuje trening modelu verbose=False powoduje, że model podczas uczenia
# nie wypisuje żadnych informacji.
clf_xgbr.fit(train_X, y_train, verbose=False)

# Dokonujemy predykcji dla danych testowych (walidacyjnych) przy użyciu XGBClassifier.
predictions = clf_xgbr.predict(test_X)

print("Mean Absolute Error dla danych walidacyjnych : " + str(mean_absolute_error(predictions, y_test)))

# Dokonujemy predykcji dla konursowych danych testowych przy użyciu XGBClassifier.
predictions_kaggle = clf_xgbr.predict(test_kaggle_X)

# Tworzymy DataFrame z predykcją dla konkursowych danych testowych.
# Dodanie ""Id" : test_kaggle["Id"].values" jest niezbędne ponieważ Kaggle wymage
# tego aby pierwsza kolumna zawierała "Id".
predictions_df = pd.DataFrame({"Id" : test_kaggle["Id"].values, "SalePrice" : predictions_kaggle})

# Zapisujemy DataFrame z predykcją dla konkursowych danych testowych do pliku csv.
predictions_df.to_csv("submission2.csv", index=False)


# Przykład cross-validacji:

# Tworzymy "scorer" czyli funkcje oceniającą
scorer = make_scorer(mean_absolute_error)

# Definiujemy podział danych na 10 części, polecam artykuł:
# https://machinelearningmastery.com/k-fold-cross-validation/
kfold = KFold(n_splits=10, random_state=11)

# Dokonuj  cross walidacji. Poniższa linijka stworzy nam 10 modeli za każdym razem inne 10%
# danych zostanie użyte jako dane testowe. W tym przypadku mogliśmy wywołać:
# results = cross_val_score(clf_xgbr, train_X, y_train, cv=10, scoring="neg_mean_absolute_error")
# bez "kfold" i bez "scorer" i obie linijki wykonają dokładnie to samo. Definiowanie oddzielnych
# "kfold" przydaje się wtedy gdy zależy nam na innym niż losowym podziale danych
# (przykładowo cross-validacja dniami tygodnia traktująca każdy z dni tygodnia jako test set).
# Definiowanie własnego "scorer" pozwala samemu zdefiniować funkcje oceny jakości modelu.
results = cross_val_score(clf_xgbr, train_X, y_train, cv=kfold, scoring=scorer)

# Wypisujemy wynik cross-validacji.
print(results)
