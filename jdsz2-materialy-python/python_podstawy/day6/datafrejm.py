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
df = pd.DataFrame(
    np.random.randn(6,4),
    index=list('123456'),
    columns=list('ABCD')
)
print(df)


#sys.exit(0)

daty = pd.date_range('20190101', periods=6, freq='Q')
df = pd.DataFrame(
    np.random.randn(6,4),
    index=daty,
    columns=list('ABCD')
)
print(df)
#sys.exit(0)
# DataFrame jako słownik
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20190102'),
                     'C' : pd.Series(1, index=list(range(8)), dtype='float32'),
                     'D' : np.array([3] * 8, dtype='int32'),
                     'E' : pd.Categorical(["testuj", "ucz", "testuj", "ucz", "testuj", "ucz", "testuj", "ucz"]),
                     'F' : 'napis'},
                   columns=['A', "C", "E", "zzz"],
                   index=[1,3,6,7,8,10,11,2]
                )
print("\nSeria\n", pd.Series(1, index=list(range(8)), dtype='float32'))
print("\narray\n", np.array([3] * 18, dtype='int32'))
print("\nDataFrame za słownika:")
print(df2)
print(df2.info())
print(df2.describe())

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
print("====================================================")
print("\ndf\n", df)
print("\nhead()\n", df.head(3))
#print(df.tail())
print("\nindexy wierszy\n", df.index)
print("\nindexy kolumn\n", df.columns)
print("\nwartosci\n", df.values)
#print("\nstatystyki\n",df.describe())

print("\nsrednia dla kolumny\n",df.mean())
print("\nsrednia dla wiersza\n", df.mean(1))

#sys.exit(0)
# Sortowanie
print("\ndf\n", df)
print("\ndf index\n", df.sort_index(axis=1, ascending=False))
print("\ndf wartosci\n", df.sort_values(by='B'))
#sys.exit(0)

# Wybieranie
print("\ndf A\n", df[ ['A', 'B'] ])
print("\ndf loc\n", df.loc["20190930", ["A", "B"]])

# Zapis
df.at[daty[0],'A'] = 3000
df.iat[3, 1] = 50000
print("\ndf\n", df)

# elementy nan
df1 = df[df > 0]
print("\ndf1\n", df1)

print("\ndrop NA\n",df1.dropna(how='any'))
print("\ndf1\n", df1.fillna(value=555))

pd.isna(df1)
#sys.exit(0)


#s.str.lower()
#pd.concat()
#df.groupby()

df = pd.DataFrame(
    {"id":[1,2,3,4,5,6],
     "wartosci":['a', 'b', 'b', 'a', 'a', 'e']}
    )
print("\ndf\n", df)
df["typ"] = df["wartosci"].astype("category")
print("\ndf\n", df.info())
df["typ"].cat.categories = ['typ1', 'typ2', 'typ3']
print("\ndf typy\n", df)


print("\ndf grupuj\n", df.groupby("typ").count())



print ("\n==============================\n")
data = pd.read_csv("exams.csv")
print(data)
print("\ndla bazy\n", data.mean()['reading score'])
print("\ndla plci\n", data.groupby(["gender", 'race/ethnicity']).mean()['reading score'])

df2 = data.groupby(["gender", 'race/ethnicity']).mean()['reading score']

print("\n\n\nindexy\n", df2.index)


levels=[
           ['female', 'male'],
           ['group A', 'group B', 'group C', 'group D', 'group E']
       ]

print("\nfemale\n", df2['male'][3])

"Zmienic grupowanie po 1k 'race/ethnicity' + 2k 'lunch' i policzyc srednia z  wynikow dla wynikow > 50 'reading score' "
data = pd.read_csv("exams.csv")
data = data[data['reading score'] > 50]
wynik = data.groupby(["race/ethnicity", 'lunch']).mean()['reading score']
print("\n===============\n", wynik)
#df[""].cat.categories = []
#df.sort_values(by="")
#df.groupby("")

sys.exit(0)
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

plt.legend(loc='best')
plt.show()
