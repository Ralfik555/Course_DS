
from sklearn.datasets import load_wine
import pandas as pd
import numpy as np
from sklearn import preprocessing
from matplotlib import pyplot as plt


#######-------------------------- NORMALIZACJA -----------------------

data = load_wine()
df = pd.DataFrame(data.data,columns = data.feature_names)

###----------- Z score --------
std_scale = preprocessing.StandardScaler().fit(df[['alcohol', 'malic_acid']])
df_std = std_scale.transform(df[['alcohol', 'malic_acid']])

##--------- min max
minmax_scale = preprocessing.MinMaxScaler().fit(df[['alcohol', 'malic_acid']])
df_minmax = minmax_scale.transform(df[['alcohol', 'malic_acid']])

print('z score \n',pd.DataFrame(df_std).describe(),'\n')
print('min max \n',pd.DataFrame(df_minmax).describe(),'\n')

###------------ wykresy ----------------------

plt.figure(figsize=(12,8))

plt.scatter(df['alcohol'], df['malic_acid'],
        color='green', label='input scale', alpha=0.5)

plt.scatter(df_std[:,0], df_std[:,1], color='red',
        label='Standardized', alpha=0.3)

plt.scatter(df_minmax[:,0], df_minmax[:,1],
        color='blue', label='min-max scaled', alpha=0.3)

plt.title('alcohol and malic_acid content of the wine dataset')
plt.xlabel('alcohol')
plt.ylabel('malic_acid')
plt.legend(loc='upper left')
plt.grid()

plt.tight_layout()
plt.show()

