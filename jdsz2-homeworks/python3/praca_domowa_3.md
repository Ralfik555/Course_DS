# Praca domowa Python nr 3
## Zadanie 1
Napisa� funkcj�, kt�rej argumentem b�dzie nazwa kraju a w wyniku otrzymamy jego stolic� oraz kod telefoniczny kraju, korzystaj�c z wikipedii.
Przyk�adowy wynik programu:
```python
Panstwo:Szwecja, Stolica:Sztokholm, kod telefoniczny:+46
```
Ponadto w przypadku, gdy nie znajdziemy informacji o danym pa�stwie b�d� wpiszemy tytu� artyku�u nie dotycz�cy pa�stwa, powinien pojawi� si� stosowny komunikat w konsoli korzystaj�c z modu�u logging. Podobnie stosowny komunikat powinien si� pojawi� w przypadku, gdy b�dzie niepoprawny adres url.

***Podpowied�*** :
Po pobraniu ca�ego html jako string, warto usun�� znaki ko�ca linii, mo�na skorzysta� z nast�puj�cego kodu:
```python
html = html.replace("\r","")
html = html.replace("\n","")
```

## Zadanie 2
W pliku *Datafiniti_Fast_Food_Restaurants.csv* znajduj� si� dane z adresami restauracji fast food w USA. Utworzy� funkcj�, kt�rej argumentem b�dzie nazwa fast fooda a w wyniku otrzymamy plik w bie��cej lokalizacji o formacie json. Kluczem ma by� nazwa fast fooda a warto�ci� lista s�ownik�w, w kt�rych kluczem b�dzie adres a warto�ci� s�ownik o kluczach  "lat" (float) ,"long" (float)
Przyk�adowy s�ownik:
```python
{"McDonald's": [{"1224 State St": {"lat": 42.79792, "long": -73.924364}},{"1232 Ulster Ave": {"lat": 41.967079, "long": -73.988583}},...]}
```
W przypadku, gdy nie znajdziemy podanej nazwy, funkcja powinna to zakomunikowa�

***Uwaga*** :
plik csv otworzy� w kodowaniu "utf8"
plik musi by� wczytywany standardowo z bie��cej lokalizacji.
