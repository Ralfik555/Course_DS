
import patsy
import pandas as pd
from sklearn.datasets import load_boston
import numpy as np

data = load_boston()


###-------- utworzenie data frame ---------
df = pd.DataFrame(data.data,columns=data.feature_names)
df['target'] = data.target

#------- deinicja formuły (bez spacji w nazwach zmiennych !!!!!) ----
f = 'target ~ CRIM + ZN * CRIM'

###----------- otrzymanie y i X z formuły -----------
y, X = patsy.dmatrices(f, df, return_type='matrix')
X


###-------- titatnic -----------


df = pd.read_csv('train.csv')

#------- deinicja formuły (bez spacji w nazwach zmiennych !!!!!) ----
f = 'Survived ~ Embarked * Sex'

###----------- otrzymanie y i X z formuły -----------
y, X = patsy.dmatrices(f, df, return_type='matrix')
X
np.asarray(X)

