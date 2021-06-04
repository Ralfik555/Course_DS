import json

lista = [1,2,3,4,5]
sl = {
    'k1': lista,
    'klucz2': "napis ssss"
}

print(lista)
print(json.dumps(lista))

class A:
    x = 6
    y = 10
obiekt_a = A()
#json.dumps(obiekt_a)

with open("json.dump", "r") as plik:
    #json.dump(sl, plik)
    slownik1 = json.load(plik)
    print(slownik1, slownik1["k1"][3])
