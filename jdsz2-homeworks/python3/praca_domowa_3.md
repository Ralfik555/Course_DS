# Praca domowa Python nr 3
## Zadanie 1
Napisaæ funkcjê, której argumentem bêdzie nazwa kraju a w wyniku otrzymamy jego stolicê oraz kod telefoniczny kraju, korzystaj¹c z wikipedii.
Przyk³adowy wynik programu:
```python
Panstwo:Szwecja, Stolica:Sztokholm, kod telefoniczny:+46
```
Ponadto w przypadku, gdy nie znajdziemy informacji o danym pañstwie b¹dŸ wpiszemy tytu³ artyku³u nie dotycz¹cy pañstwa, powinien pojawiæ siê stosowny komunikat w konsoli korzystaj¹c z modu³u logging. Podobnie stosowny komunikat powinien siê pojawiæ w przypadku, gdy bêdzie niepoprawny adres url.

***PodpowiedŸ*** :
Po pobraniu ca³ego html jako string, warto usun¹æ znaki koñca linii, mo¿na skorzystaæ z nastêpuj¹cego kodu:
```python
html = html.replace("\r","")
html = html.replace("\n","")
```

## Zadanie 2
W pliku *Datafiniti_Fast_Food_Restaurants.csv* znajduj¹ siê dane z adresami restauracji fast food w USA. Utworzyæ funkcjê, której argumentem bêdzie nazwa fast fooda a w wyniku otrzymamy plik w bie¿¹cej lokalizacji o formacie json. Kluczem ma byæ nazwa fast fooda a wartoœci¹ lista s³owników, w których kluczem bêdzie adres a wartoœci¹ s³ownik o kluczach  "lat" (float) ,"long" (float)
Przyk³adowy s³ownik:
```python
{"McDonald's": [{"1224 State St": {"lat": 42.79792, "long": -73.924364}},{"1232 Ulster Ave": {"lat": 41.967079, "long": -73.988583}},...]}
```
W przypadku, gdy nie znajdziemy podanej nazwy, funkcja powinna to zakomunikowaæ

***Uwaga*** :
plik csv otworzyæ w kodowaniu "utf8"
plik musi byæ wczytywany standardowo z bie¿¹cej lokalizacji.
