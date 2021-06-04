class Owoc:
    kolor = 'żółty'
    smak = 'słodki'
    ilosc = 0

    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
        Owoc.ilosc += 1
        print("utworzono obiekt {}".format(nazwa))

    def zmien_kolor(self, kolor):
        self.kolor = kolor

    def __str__(self):
        return "jestem {}".format(self.nazwa)


class Banan(Owoc):
    narkotyki = False

    def sprawdz_narkotyki(self):
        if self.narkotyki:
            print("znaleziono narkotyki!")
            self.cena = 50000
        else:
            print("nie ma narkotyków")


def popraw_kolor(owoc):
    if owoc.nazwa == "gruszka":
        if owoc.kolor == "żółty":
            print("kolor gruszki jest ok")
        else:
            print("zmiana koloru gruszki")
            owoc.zmien_kolor("zółty")
    elif owoc.nazwa == "jabłko":
        if owoc.kolor == "czrwony":
            print("kolor gruszki jest ok")
        else:
            print("zmiana koloru jabłka na czerwony")
            owoc.zmien_kolor("czerowny")


print("ile mamy owoców?", Owoc.ilosc)

gruszka = Owoc("gruszka", 5)
jablko = Owoc("jabłko", 3)
ananas = Owoc("ananas", 8)

print("ile mamy owoców?", Owoc.ilosc)

print("kolor jabła i gruszki przed zmianą:", jablko.kolor, gruszka.kolor)
popraw_kolor(gruszka)
popraw_kolor(jablko)
print("kolor jabła i gruszki po zmianach:", jablko.kolor, gruszka.kolor)

print(jablko)

banan = Banan("banan", 4)
banan2 = Banan("banan", 15)
banan2.narkotyki = True
print("ile mamy owoców?", Owoc.ilosc)

banan.sprawdz_narkotyki()
banan2.sprawdz_narkotyki()