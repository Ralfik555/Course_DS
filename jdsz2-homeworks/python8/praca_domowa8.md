# Zadanie 1
Nale¿y pobraæ z sklearn.datasets zbiór diabetes. Zadanie polega na przeprowadzeniu cross walidacji z 20 foldami dla modeli xgboost z ro¿nymi parametrami. Rozwa¿aæ bêdziemy parametry:
- **max_depth** ( od 3 do 8 w³¹cznie)
- **learning_rate** (od 0.05 do 0.3 w³¹cznie, z krokiem 0.05)

£¹cznie daje nam to 36 modeli. Dla ka¿dego modelu otrzymamy wiêc 20 wartoœci mean_squered_error. Nale¿y utworzyæ DataFrame w którym bêdziemy mieli wszystkie wartoœci  mean_squere_error oraz parametry danego modelu. Poni¿ej przyk³adowa tatka tabela.

| max_depth | learning_rate | mean_squered_error |
|-----------|---------------|-------------------|
| 3         | 0.05          | 11327             |
| 3         | 0.05          | 12894             |
| 3         | 0.05          | 13818             |
| 3         | 0.05          | 10515             |
| .         | .             | .                 |
| .         | .             | .                 |
| 8         | 0.3           | 14087             |
| 8         | 0.3           | 10996             |
| 8         | 0.3           | 12189             |
| 8         | 0.3           | 11011             |

Ponadto obliczyæ minimalny oraz maksymalny b³¹d. Nastêpnie otrzymany DataFrame oraz wartoœci minimalne i maksymalne umieœciæ w jednym s³owniku i zapiklowaæ pod nazw¹ results.pickle

**podpowidŸ:**
W celu utworzenia tabeli wynikowej ³atwo jest aby na pocz¹tku utworzyæ pusty DataFrame a nastêpnie w ka¿ym przejœciu pêtli dodawaæ tymczasowy DataFrame z wynikami dla jednej cross walidacji
```python
df_cv = pd.DataFrame()
# tmp to tabela z wynikami z jednej cross validacji, w taki sposób mo¿emy dokleiæ j¹ do ju¿ istniej¹cego DataFrame z wynikami 
df_cv = df_cv.append(tmp)
```

# Zadanie 2

Utworzyæ w jupyter notebook wizualizacjê rozk³adu b³êdów œredniokwadratowych w zale¿noœci od wybranego max_depth i learning_rate.
Nale¿y wiêc wczytaæ pickle z zadania 1 i za pomoc¹ widgetu zwizualizowaæ histogram mean_squere_error, gdzie parametry max_depth i learning_rate wybierami za pomoc¹ suwaków (oczywiœcie musz¹ byæ w tych samych zakresach co te z tabeli) Pod wykresem ponadto wyœwietliæ œredni mean_squere_error.
Histogram ma byæ w zakresie minimalnego i maksymalnego b³êdu z wczytanego pikla, tak byœmy zawsze mieli t¹ sam¹ skalê odniesienia, gdy obserwujemy rozk³ad b³êdów.


