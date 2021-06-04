# Zadanie 1

Dla zmiennej ***litera*** oraz ***tekst*** stworzyć instrukcję warunkową, która będzie zwracała informację, że litera wystąpiła dokładnie jeden raz, więcej niż raz bądź wcale.
Przykładowo:
```python
litera = 'a'
tekst = 'ala ma kota'
```
Wynik:
```python
'W tekście: ala ma kota, litera a występuje więcej niż jeden raz.'
```
W princie należy użyć zmiennych litera oraz tekst.
**Uwaga!** Proszę o nie używanie w kodzie polskich znaków ó, ś, ę itp
# Zadanie 2
Mamy dany słownik, w którym znajdują się informację o przynależności pracowników do danych działów w firmie.
```python
firma = {'IT':['Kacper Nowak','Blazej Wojcik','Aneta Kowalska'],
'Kadry':['Krzysztof Kaminski','Anna Wisniewska','Danuta Zielinska','Daria Szymanska'],
'Ksiegowosc':['Mirek Wozniak','Lukasz Dabrowski','Katarzyna Jankowska'],
'Sprzedaz':['Leszek Wojciechowski','Danuta Mazur','Kacper Kowalski','Anna Piotrowska','Katarzyna Grabowska']}
```
Wyobraźmy sobie, że tworzymy system kadrowy do zarządzania strukturą w firmie. Mamy funkcjonalność dodawania nowego pracownika, jeżeli nie ma takiego w firmie oraz mamy możliwość przenoszenia obecnych pracowników z ich dotychczasowych działów do innych (już istniejących).

Mamy zmienne: ***pracownik***, ***dzial_nowy***, ***dzial_stary***
Gdy pracownik jest nowy należy umieścić w ***dzial_nowy***. Natomiast gdy pracownik jest już w firmie, przenieść do z ***dzial_stary*** do ***dzial_nowy***. Oprócz dodania lub przeniesienia również musi pojawić się komunikat informacyjny o wykonanej akcji. Powinien również pojawić się stosowny komunikat w momencie, gdybyśmy chcieli przenieść pracownika z działu, w którym nie pracuje.

Przykładowe działanie:
```python
pracownik = 'Leszek Wojciechowski'
dzial_nowy = 'Kadry'
dzial_stary = 'IT'
```
Wynik programu:
```python
'Pracownik Leszek Wojciechowski nie pracuje w dziale IT  - operacja przeniesienia do innego dzialu nie jest mozliwa'
```
**Uwaga!**
W operacji przenoszenia należy użyć funkcji pop. Ponadto zakładamy, że wartość zmiennych ***dzial_nowy***, ***dzial_stary*** pochodzą z listy rozwijalnej i są zawsze poprawne - moglibyśmy sobie wyobrazić aplikację,  w której te dwie zmienne wybieramy za pomocą takiej listy. Natomiast zmienną ***pracownik*** wpisujemy ręczne – w aplikacji mogłoby to być pole tekstowe. Zatem należy zabezpieczyć to pole przed różną wielkością znaków np. jak wpiszemy „kacper nowak” lub „KACPER  NOWAK „ to będzie to obecny, nie nowy pracownik. Analogicznie gdy wpiszemy przykładowo „jan kowalski” to program ma wpisać nam nowego pracownika do słownika zachowując dotychczasową konwencję.

Dla chętnych:
Dodać funkcjonalność dodawania nowych działów i kasowanie obecnych. Należy uwzględnić że nie można usunąć działu, w którym są obecni pracownicy. Zatem można zablokować kasowanie gdy są pracownicy lub dodać funkcjonalność kasowania działu z jednoczesnym przeniesieniem wszystkich pracowników tego działu do innego. Również można dodać funkcjonalność usuwania pracownika.
