# Zadanie 1

Zbiór california_hausing podzielić na treningowy i testowy. Dla zmiennych Population i HouseAge przeprowadzić standaryzację (łącznie z usunięciem outliersów)  na zbiorze treningowym. Ponadto wyliczyć dla każdej zmiennej parametry, które posłużyły do standaryzacji (średnia i odchylenie std) i zapisać do słownika. Przykładowy słownik:
```python
stats = {'Population':{'avg':122,'sd':34},...}
```
Na ustandaryzowanym zbiorze treningowym utworzyć modell ball tree. Następnie taki model zapiklować do pliku z rozszerzeniem .pickle wraz ze słownikiem ze statystykami standaryzacji.
Następnie wczytując ten plik wypisać 5 najbliższych sąsiadów (ich indeksy) dla dowolnej obserwacji ze zbioru testowego. Oczywiście tą obserwację należy najpierw ustandaryzować wg parametrów zapisanych w pliku.

# Zadanie 2
Na podstawie slajdu 18 z prezentacji dowiedzieć się jakie parametry ma RandomForestClassifier() a następnie w pliku:
will-it-rain-tomorrow.py
postarać się uzyskać jak najlepszy "Accuracy" dla test setu eksperymentując właśnie z tymi parametrami.
