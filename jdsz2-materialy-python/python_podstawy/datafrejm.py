import sys
import pandas as pd
import numpy as np


s = pd.Series([1, 3, 5, np.nan, 6, 8])
#s = pd.Series([1, 2, 3, 4, 5, 6], index=list('123456'))
#s = pd.Series(np.random.randint(0, 7, size=30))
print("Series:")
print(s)
#print(s.value_counts())

print("\nDataFrame:")
#df = pd.DataFrame(np.random.randn(10, 4))
df = pd.DataFrame(np.random.randn(6,4), index=list('123456'), columns=list('ABCD'))
print(df)

daty = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=daty, columns=list('ABCD'))
#print(df)

# DataFrame jako słownik
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20190102'),
                     'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                     'D' : np.array([3] * 4, dtype='int32'),
                     'E' : pd.Categorical(["testuj", "ucz", "testuj", "ucz"]),
                     'F' : 'napis'})
print("\nDataFrame za słownika:")
print(df2)

df3 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20190102'),
                     'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                     'D' : np.array([3] * 4, dtype='int32'),
                     'E' : pd.Categorical(["testuj", "ucz", "testuj", "ucz"]),
                     'F' : 'napis'},
                   index = ['rząd1', 'rząd2', 'rząd3', 'rząd4'])
print("\nDataFrame za słownika z podanymi indeksami:")
print(df3)

df4 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20190102'),
                     'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                     'D' : np.array([3] * 4, dtype='int32'),
                     'E' : pd.Categorical(["testuj", "ucz", "testuj", "ucz"]),
                     5: "wiersz1",
                     'F' : 'napis'},
                   index = ['rząd1', 'rząd2', 'rząd3', 'rząd4'],
                   columns = ['kolumna1', 'B', 'c', 5, 6, 'ostatnia']
                   )
print("\nDataFrame za słownika z podanymi indeksami i kolumnami:")
print(df4)

df5 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20190102'),
                     'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                     'D' : np.array([3] * 4, dtype='int32'),
                     'E' : pd.Categorical(["testuj", "ucz", "testuj", "ucz"]),
                     5: "wiersz1",
                     'F' : 'napis'},
                   index = pd.MultiIndex.from_tuples(
                       [('GR1', 'rząd1'), ('GR1', 'rząd2'), ('GR1', 'rząd3'), ('GR2', 'rząd4')],
                        names=["grupa", "index"]
                   ),
                   columns = ['kolumna1', 'B', 'c', 5, 6, 'ostatnia']
                   )
print("\nDataFrame za słownika z pogrupowanymi indeksami:")
print(df5)

#sys.exit(0)

print("\nhead()\n", df.head())
#print(df.tail())
print("\nindexy wierszy\n", df.index)
#print(df.columns)
#print(df.values)
print("\nopis\n", df.info())
print("\nstatystyki\n", df.describe())
#print(df.mean())
#print(df.mean(1))
#unique()
#value_counts()

#sys.exit(0)

# Sortowanie
print("\n======== Sortowanie ========\nPrzed:\n", df)
print("\nKolumny:\n", df.sort_index(axis=1, ascending=False))
print("\nPo wartości:\n", df.sort_values(by='B'))

#sys.exit(0)

# Wybieranie
print("\n======== Wybieranie ========\nPrzed:\n", df, "\n")
print(df[df>0])
#df.iloc[,]
#df.loc[,]

#sys.exit(0)

# Zapis
#df.at[daty[0],'A'] = 0
#df.iat[0,1] = 0

#sys.exit(0)

# elementy nan
#df1.dropna(how='any')
#df1.fillna(value=0)
#pd.isna(df1)

print("\n======== Operacje ========\nPrzed:\n", df, "\n")
#s.str.lower()
#pd.concat()
#pivot
#melt

#sys.exit(0)

print("\n======== Grupowanie ========\nPrzed:\n", df, "\n")
#df.groupby()

#df = pd.DataFrame({"id":[1,2,3,4,5,6], "":['a', 'b', 'b', 'a', 'a', 'e']})
#df[""] = df[""].astype("category")
#df[""].cat.categories = []
#df.sort_values(by="")
#df.groupby("")
#groups / get_group
#agg
#sys.exit(0)

# ====================================================================
# Wykresy
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2010', periods=1000))
ts = ts.cumsum()
#print("\nDane do wykresu 1")
#print(ts)
ts.plot()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['firma 1', 'firma 2', 'firma 3', 'firma 4'])
df = df.cumsum()
#print("\nDane do wykresu 2")
#print(df)

plt.figure();
df.plot();
##bar
#hist
#stacked

plt.legend(loc='best')
plt.show()