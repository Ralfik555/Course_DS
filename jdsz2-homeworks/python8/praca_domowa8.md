# Zadanie 1
Nale�y pobra� z sklearn.datasets zbi�r diabetes. Zadanie polega na przeprowadzeniu cross walidacji z 20 foldami dla modeli xgboost z ro�nymi parametrami. Rozwa�a� b�dziemy parametry:
- **max_depth** ( od 3 do 8 w��cznie)
- **learning_rate** (od 0.05 do 0.3 w��cznie, z krokiem 0.05)

��cznie daje nam to 36 modeli. Dla ka�dego modelu otrzymamy wi�c 20 warto�ci mean_squered_error. Nale�y utworzy� DataFrame w kt�rym b�dziemy mieli wszystkie warto�ci  mean_squere_error oraz parametry danego modelu. Poni�ej przyk�adowa tatka tabela.

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

Ponadto obliczy� minimalny oraz maksymalny b��d. Nast�pnie otrzymany DataFrame oraz warto�ci minimalne i maksymalne umie�ci� w jednym s�owniku i zapiklowa� pod nazw� results.pickle

**podpowid�:**
W celu utworzenia tabeli wynikowej �atwo jest aby na pocz�tku utworzy� pusty DataFrame a nast�pnie w ka�ym przej�ciu p�tli dodawa� tymczasowy DataFrame z wynikami dla jednej cross walidacji
```python
df_cv = pd.DataFrame()
# tmp to tabela z wynikami z jednej cross validacji, w taki spos�b mo�emy doklei� j� do ju� istniej�cego DataFrame z wynikami 
df_cv = df_cv.append(tmp)
```

# Zadanie 2

Utworzy� w jupyter notebook wizualizacj� rozk�adu b��d�w �redniokwadratowych w zale�no�ci od wybranego max_depth i learning_rate.
Nale�y wi�c wczyta� pickle z zadania 1 i za pomoc� widgetu zwizualizowa� histogram mean_squere_error, gdzie parametry max_depth i learning_rate wybierami za pomoc� suwak�w (oczywi�cie musz� by� w tych samych zakresach co te z tabeli) Pod wykresem ponadto wy�wietli� �redni mean_squere_error.
Histogram ma by� w zakresie minimalnego i maksymalnego b��du z wczytanego pikla, tak by�my zawsze mieli t� sam� skal� odniesienia, gdy obserwujemy rozk�ad b��d�w.


