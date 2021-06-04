# ZADANIE1: sumowanie liczb o 1 do 100 aż suma przekroczy sto i podaje ile liczb zostało dodanych
suma = 0
for liczba in range(100):
    suma += liczba
    if suma > 100:
        break

print("Suma przekroczyła 100 ({}) po dodaniu {} liczb".format(suma, liczba))

# ZADANIE2: Sprawdzić po dodaniu ilu elementów ciągu Fibonacciego ich suma przekroczy 5000
SUMA_MAX = 5000
policz = 1
ile = 0
element_poprzedni = 0
element_biezacy = 1

while suma <= SUMA_MAX:
    tymczasowy = element_biezacy
    element_biezacy += element_poprzedni
    element_poprzedni = tymczasowy
    suma += element_biezacy
    policz += 1

print("Suma przekorczyła {} ({}) po zsumowaniu {} elementów ciągu Fibonacciego".format(SUMA_MAX, suma, policz))