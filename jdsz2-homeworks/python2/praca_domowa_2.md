# Zadanie 1
W poprzednim zadaniu struktura firmy była oparta na słowniku, opisującym przynależność do poszczególnych działów:
```python
firma = {'IT':['Kacper Nowak','Blazej Wojcik','Aneta Kowalska'],
'Kadry':['Krzysztof Kaminski','Anna Wisniewska','Danuta Zielinska','Daria Szymanska'],
'Ksiegowosc':['Mirek Wozniak','Lukasz Dabrowski','Katarzyna Jankowska'],
'Sprzedaz':['Leszek Wojciechowski','Danuta Mazur','Kacper Kowalski','Anna Piotrowska','Katarzyna Grabowska']}
```
Firma postanowiła jednak wprowadzić kilka zmian w systemie kadrowym, aby w inny sposób zarządzać pracownikami.

Poproszono nas o stworzenie nowego rozwiązania opartego na klasach:
* każdy pracownik miałby być obiektem tej samej klasy co inni
* każdy pracownik ma imię, nazwisko, przypisaną nazwę działu, w którym pracuje oraz pensję (3000zł)
* każdy pracownik ma mieć możliwość:
    * dostania podwyżki:
        * pensja nie może być obniżona
        * pensja nie może przekroczyć 10000 zł
    * zmiany działu:
        * nie można zmienić na dział w którym już się jest

Wszystkich pracowników należy przenieść do nowej technologii i umieścić w nowej 'bazie', za pomocą funkcji **transferuj()**. Nowa baza powinna być listą pracowników, gdzie każdy element jest oddzielnym obiektem pracownika. Po przeniesieniu, dawna baza **firma** powinna zostać wyczyszczona.
UWAGA: w starej bazie imię i nazwisko jest razem, teraz będą stanowić oddzielne pola. Można skorzystać z funkcji **split()**. Proszę też o zastosowanie przekazywania nazwiska do obiektu przez 'rozpakowanie' listy.

Należy następnie napisać funkcję wyszukiwania pracowników po nazwisku i jeśli pracownik się odnajdzie to powinien się przedstawić: podac imię, nazwisko, dział oraz pensję.

Należy napisać funkcję, która da podwyżki wszystkim pracownikom danego działu. Podajemy dział oraz kwotę. Proszę o zabezpieczenie funkcji przed podaniem błędnych typów wartości.
