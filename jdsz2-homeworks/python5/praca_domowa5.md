## Zadanie 1
Pobra� z modu�u sklearn.datasets zbi�r diabetes (load_diabetes). Nast�pnie dla ka�dej zmiennej narysowa� wykres rozrzutu wraz z dopasowan� lini� regrsji oraz wy�wietli� podstawowe statystyki modelu: coef,std err,t, p-value. Kod ma dzi�a� w p�tli oraz zadzia�a� r�wnie� gdy wybierzemy zbi�r boston (load_boston)
***Podpowied�***
do wy�wietlenia statystyk polecam u�y� modu�u statsmodels.formula.api

## Zadanie 2
Pobra� z modu�u sklearn.datasets zbi�r wine (load_wine). Zbi�r podzieli� na ucz�cy, walidacyjny oraz testowy (proporcje 60% 20% 20%) . Nast�pnie nauczy� na zbiorze ucz�cym model regresji logistycznej oraz drzewa decyzyjnego. Dla obu modeli na zbiorze walidacyjnym wyliczy� miar� F1 i na jej podstawie wybra� lepiszy model. Na ko�cu zrobi� predykcj� wybranym modelem na zbiorze testowym i sprawdzi� statystyki precision, recall i f1 - te� wy�wietli� jaki model zosta� wybran.
***Podpowied�***
Do podj�cia decyzji warto u�y� funkcji classification_report() z parametrem *output_dict=True*


