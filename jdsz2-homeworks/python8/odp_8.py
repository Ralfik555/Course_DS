
from xgboost import XGBRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import  load_diabetes
import numpy as np
import pickle 

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer
from sklearn.metrics import mean_squared_error

##---- pobrane danych ----------
data =load_diabetes()
X = data.data
Y = data.target

##-------- listy z parametrami do sprawdzenia ---------
md_list = list(range(3,9))
lr_list = np.arange(0.05,0.31,0.05)

##-------- tworzymy pusty data frame wynikowy ---
df_cv = pd.DataFrame()

k = 0
for m in md_list:
    for l in lr_list:
        clf_xgbr = XGBRegressor(max_depth = m ,learning_rate = l)
        scorer = make_scorer(mean_squared_error)
        kfold = KFold(n_splits=20, random_state=11)
        results = cross_val_score(clf_xgbr, X, Y, cv=kfold, scoring=scorer)
        ##------- tworzymy tymczasowy data frame z wynikami 1 modelu
        tmp = pd.DataFrame({"mse":results})
        tmp['max_depth'] = m
        tmp['learning_rate'] = l
        ##--------- wrzucamy data frame tymaczosy do wynikowego ----
        df_cv = df_cv.append(tmp)
        ##---- wywietlenie postepu -----
        k +=1
        print('{0}/{1} done'.format(k,len(md_list)*len(lr_list)) )

min_error = min(df_cv['mse'])
max_error = max(df_cv['mse'])

##------- słownik wynikowy ----------
out = {"df":df_cv,"min_error":min_error,"max_error":max_error}
##-------- zapisanie do pickla
with open('result.pickle', 'wb') as f:
    pickle.dump(out, f)




