# Zadanie 1
litera = 'a'
tekst = 'ala ma kota'

if (tekst.find(litera) >= 0):
    if (tekst[tekst.find(litera) + 1:].find(litera) >= 0):
        print('W tekscie: "', tekst, '" litera', litera, 'wystepuje wiecej niz jeden raz')
    else:
        print('W tekscie:"', tekst, '" litera', litera, 'wystepuje dokladnie jeden raz')
else:
    print('W tekscie:"', tekst, '" litera', litera, 'nie wystepuje')


# Zadanie 2
firma = {'IT': ['Kacper Nowak', 'Blazej Wojcik', 'Aneta Kowalska'],
        'Kadry': ['Krzysztof Kaminski', 'Anna Wisniewska', 'Danuta Zielinska', 'Daria Szymanska'],
        'Ksiegowosc': ['Mirek Wozniak', 'Lukasz Dabrowski', 'Katarzyna Jankowska'],
        'Sprzedaz': ['Leszek Wojciechowski', 'Danuta Mazur', 'Kacper Kowalski', 'Anna Piotrowska', 'Katarzyna Grabowska']
}

pracownik = 'Leszek Wojciechowski'
pracownik = pracownik.title()

dzial_nowy = 'Kadry'
dzial_stary = 'IT'

firma_cala = firma['IT'] + firma['Kadry'] + firma['Ksiegowosc'] + firma['Sprzedaz']

if (pracownik in firma_cala):
    if (pracownik in firma[dzial_stary]):
        firma[dzial_nowy].append(firma[dzial_stary].pop(firma[dzial_stary].index(pracownik)))
        print('Pracownika', pracownik, 'przeniesiono z dzialu', dzial_stary, 'do dzialu', dzial_nowy)
    else:
        print('Pracownik', pracownik, 'nie pracuje w dziale', dzial_stary,
          ' - operacja przeniesienia do innego dzialu nie jest mozliwa')
else:
    firma[dzial_nowy].append(pracownik)
    print('Dodano nowego pracownika', pracownik, 'do dzialu', dzial_nowy)
