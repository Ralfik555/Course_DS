


#####------------------------ ZAD 1 ---------------------------------

import sys
import pandas as pd
import numpy as np


data = pd.read_csv("exams.csv")

df = data.groupby(['gender','lunch']).mean()

def reindex_df(df):
    n = 1
    for n in range(len(df.index.names)):
        vals = []
        i = 0
        for i in range(len(df)):
            vals.append(df.index[i][n])
        df[df.index.names[n]] = vals
    df.index = range(len(df))
    return(df)    
    

df2 = reindex_df(df)

#####------------------------ ZAD 2 ---------------------------------

###---------- WCZYTANIE DANYCH, MODEL, PREDUKCJE --------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np

pd.set_option("display.max_columns", 10)

dataset=pd.read_csv('train.csv')

X=dataset.drop('price_range',axis=1)
y=dataset['price_range']

train_X, val_X, train_y, val_y  = train_test_split(X, y, random_state=101)

model = KNeighborsClassifier(n_neighbors=20)
model.fit(train_X, train_y)

preds_val = model.predict(val_X)
print(classification_report(val_y, preds_val))



values = val_y.as_matrix()


####-------------------- confusion_matrix -------------

def conf_mx(y,predict):
    lvls = list(set(y))
    mx = []
    for i in range(len(lvls)):
        x = []
        for j in range(len(lvls)):
            idx_y = list(y == lvls[i])
            idx_p = list(predict == lvls[j])
            tab = pd.DataFrame({'y':idx_y,'p':idx_p})
            t = tab[ (tab['y'] )  & ( tab['p'] )]
            x.append(len(t))
        mx.append(x)    
    return(np.matrix(mx))
    
##--------- z pakietu ---------------   
matrix = confusion_matrix(val_y, preds_val)
print(matrix)
# ---------- moja funkcja ------------
print(conf_mx(values,preds_val))


####-------------------- classification_report -------------

y,predict = values,preds_val

def class_report(y,predict):
    lvls = list(set(y))
    pr_v = []
    rec_v =[]
    f1_v = []
    for i in range(len(lvls)):
        precision = sum( (y == lvls[i]) & (predict == lvls[i]) ) / sum( (predict == lvls[i]))
        recall = sum( (y == lvls[i]) & (predict == lvls[i]) ) / sum( (y == lvls[i]))
        f1 = 2* ((precision * recall) / (precision + recall) )
        pr_v.append(round(precision,2))
        rec_v.append(round(recall,2))
        f1_v.append(round(f1,2))
    tab=pd.DataFrame({'precision':pr_v,'recall':rec_v,'f1':f1_v},index=lvls)    
    return(tab)

print(classification_report(val_y, preds_val))
print(class_report(val_y, preds_val))



