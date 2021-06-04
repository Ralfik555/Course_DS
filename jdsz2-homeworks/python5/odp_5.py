
##########------------ ZADANIE 1 ------------------------

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from sklearn import datasets
from sklearn.metrics import r2_score
from statsmodels.api import OLS

dane = datasets.load_boston()
df = pd.DataFrame(dane['data'], columns=dane.feature_names)


for i in df.columns:
    x,y = df[i], dane['target']
    n,p =df.shape
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    y_ = x * slope + intercept

    print(df[i].name)
    plt.figure(1, figsize=(10, 10))
    plt.scatter(x.ravel(), y, color='black')
    plt.ylabel('y')
    plt.xlabel('X')
    plt.title(i)
    plt.plot(x, y_, linewidth=1)
    plt.show()
    
    print(OLS(y, x).fit().summary().tables[1])
    
##########------------ ZADANIE 2 ------------------------  

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report, f1_score

dataset = datasets.load_wine()
X, y = dataset.data, dataset.target
X = X

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=10)
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.25, random_state=10)



model_lr = linear_model.LogisticRegression(random_state=0)
model_lr.fit(X_train, y_train)
predictions_lr = model_lr.predict(X_val)


model_dtr = DecisionTreeRegressor(random_state=101)
model_dtr.fit(X_train, y_train)
predictions_dtr = model_dtr.predict(X_val)


model_lr_f1 = f1_score(y_val, predictions_lr, average='weighted')
print('Dla modelu regresji logistycznej miara F1 wyliczona na zbiorze walidacyjnym wynosi: {}'.format(model_lr_f1))
#print(classification_report(y_val, predictions_lr))
model_dtr_f1 = f1_score(y_val, predictions_dtr, average='weighted')
print('Dla modelu drzewa decyzyjnego miara F1 wyliczona na zbiorze walidacyjnym wynosi: {}'.format(model_dtr_f1))
#print(classification_report(y_val, predictions_dtr))

model_lepszy = 'model regresji logistycznej' if model_lr_f1 > model_dtr_f1 else 'model drzewa decyzyjnego'
print('\nNa podstawie wyliczonej miary F1 na zbiorze walidacyjnym, jako lepszy wybrano', model_lepszy, '\n')

#Predykcja wybranym modelem na zbiorze testowym
if model_lepszy == 'model regresji logistycznej':
    predictions_test = model_lr.predict(X_test)
else:
    predictions_test = model_dtr.predict(X_test)
print('Statystyki dla wybranego modelu: {}, wyliczone na zbiorze testowym:\n'.format(model_lepszy))
print(classification_report(y_test, predictions_test))




