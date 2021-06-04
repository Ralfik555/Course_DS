firma = {'IT':['Kacper Nowak','Blazej Wojcik','Aneta Kowalska'],
        'Kadry':['Krzysztof Kaminski','Anna Wisniewska','Danuta Zielinska','Daria Szymanska'],
        'Ksiegowosc':['Mirek Wozniak','Lukasz Dabrowski','Katarzyna Jankowska'],
        'Sprzedaz':['Leszek Wojciechowski','Danuta Mazur','Kacper Kowalski','Anna Piotrowska','Katarzyna Grabowska']
}


class Pracownik:
    pensja = 3000

    def __init__(self, imie, nazwisko, dzial):
        self.imie = imie
        self.nazwisko = nazwisko
        self.dzial = dzial

    def podwyzka(self, ile):
        if ile <= 0:
            print("Nie można obniżyć pensji!")
        else:
            self.pensja += ile
            if self.pensja > 10000:
                self.pensja = 10000
                print("Pracownik osiągnł maksymalne wynagrodzenie 10tys. zł!")

    def zmiana_dzialu(self, nowy_dzial):
        if self.dzial == nowy_dzial:
            print("Nie można zmienić działu na ten sam!")
        else:
            self.dzial = nowy_dzial

    def __str__(self):
        return "Witam! Nazywam się {} {}, pracuję w dziale {} i zarabiam {}.".format(self.imie, self.nazwisko, self.dzial, self.pensja)


def transferuj():
    nowa_baza = []
    przeniesiono = 0

    for dzial in firma:
        for pracownik in firma[dzial]:
            nowa_baza.append(Pracownik(*pracownik.split(), dzial))
            przeniesiono += 1

    if len(nowa_baza) == przeniesiono:
        print("Dane przeniesiono do nowej bazy")
        firma.clear()
        print("Baza firma została wyczyszczona:", firma)
        return nowa_baza
    else:
        print("Transfer pracwoników się nie powódł!")
        return []


def szukaj_pracownika(baza, imie, nazwisko):
    print("Szukam pracownika", imie, nazwisko)
    for pracownik in baza:
        if pracownik.imie == imie and pracownik.nazwisko == nazwisko:
            print("Znaleziono pracownika:\n\t", pracownik)
            break
    else:
        print("Nie znaleziono pracwonika", imie, nazwisko)


def daj_podwyzki(baza, dzial, kwota):
    print("Podwyzki o", kwota, "zł dla wszystkich z działu", dzial)
    try:
        for pracownik in baza:
            try:
                if pracownik.dzial == dzial:
                    try:
                        pracownik.podwyzka(kwota)
                    except TypeError:
                        print("Kwota musi byc wyrożona liczbowo")
                        break
            except AttributeError:
                print("pracownik {} nie ma właściwości dział! Sprawdź bazę danych: {}".format(pracownik, baza))
    except TypeError:
        print("Nieprawidłowa baza danych!", baza)


nowa_baza = transferuj()
szukaj_pracownika(nowa_baza, "Anna", "Wisniewska")

daj_podwyzki(nowa_baza, "IT", "500")
daj_podwyzki(5, "IT", 500)
daj_podwyzki([5 ,6 ,7], "IT", 500)
daj_podwyzki(nowa_baza, "IT", 500)

