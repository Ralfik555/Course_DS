import csv

miesiac = 'lipiec'
waluta = 'dolar'
with open("publ_sredni_m_2018.csv", encoding="Windows-1250") as plik4:
    dane = csv.reader(plik4, delimiter=";")
    index = 0
    for linia in dane:
        if not index:
            index = linia.index(miesiac)
            print("index kolumny miesiaca:", index)
        if waluta in linia[0]:
            print("{} kurs na lipiec:\t{}".format(linia[0], linia[index]))
