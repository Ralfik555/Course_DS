podstawowy_vat = 23


# słownik stawek VAT wpisany ręcznie
vat = {
    0: ['obrót międzynarodowy']
}
# dodanie nowej stawki VAT z deklaracją produktów
literatura = ['książki']
vat[5] = literatura

# nowa grupa objęta VATem
budownictwo = ['budowy', 'modernizacje', 'dostawy']
# dodanie stawki VAT
vat[8] = budownictwo

#print(vat)
# rozszerzamy ulgi na budownictwo
budownictwo.append('remonty')
#print(vat)

# nowa grupa objęta VATem 5%
#print(vat[5])
# dodajemy do grupy 5%
vat[5] += ['chleb', 'produkty zbożowe', 'nabiał', 'przetwory mięsne', 'soki']

#print(vat[5])
literatura.append('czasopisma specjalistyczne')
# print(vat[5])
# print(literatura)

# print()
# lista1 =[1, 2, 3]
# lista2 = lista1
# print("lista1:", lista1)
# print("lista2:", lista2)
# lista2[1] = 555
# print("lista2 po zmianie:", lista2)
# print("lista1:           ", lista1)
# print("czy te listy to te same listy?:", lista2 is lista1)
# lista3 = lista1[:]
# print("lista3:", lista1)
# print("czy lista3 to też ta sma lista?:", lista3 is lista1)
# lista3[1] = 123
# print("lista3 po zmianie:", lista3)
# print("lista1:           ", lista1)

### ZADANIE 1 - obniżenie stawki VAT z 8 na 7

vat[7] = vat.pop(8)
print(vat)
### ZADANIE 2 - przeniesienie soków ze stawki 5 do stawki 7

vat[7] +=  [vat[5].pop(vat[5].index('soki'))]


### ZADANIE 3 - sprawdzenie jaka stawka obowiązuje na nabiał a jaka na cegły

