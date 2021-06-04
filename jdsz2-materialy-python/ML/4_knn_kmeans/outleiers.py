
from sklearn import preprocessing
import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt


from sklearn.datasets import fetch_california_housing
data = fetch_california_housing()

df = pd.DataFrame(data.data,columns = data.feature_names)

print(df['Population'].describe())


plt.title('Population')
plt.hist(df['Population'])
plt.show()

plt.title('HouseAge')
plt.hist(df['HouseAge'])
plt.show()


##--------- normalizacja z outleiersami --------
norm_scale = preprocessing.StandardScaler().fit(df[['Population', 'HouseAge']])
df_norm = norm_scale.transform(df[['Population', 'HouseAge']])

plt.figure(figsize=(10,10))
plt.scatter(df_norm[:,0], df_norm[:,1], color='blue', alpha=0.3)

##----------- usuwanie outlieres --------
quarties = np.array(df[['Population']].quantile([0.25,0.75]))
down = float(quarties[0]  - 1.5 * quarties[1]-quarties[0] )
up = float(quarties[1]  + 1.5 * quarties[1]-quarties[0] )

df_ro = df.loc[(df['Population'] > down) & (df['Population'] < up)]


norm_scale = preprocessing.StandardScaler().fit(df_ro[['Population', 'HouseAge']])
df_norm_ro = norm_scale.transform(df_ro[['Population', 'HouseAge']])

plt.figure(figsize=(10,10))
plt.scatter(df_norm_ro[:,0], df_norm_ro[:,1], color='blue', alpha=0.3)