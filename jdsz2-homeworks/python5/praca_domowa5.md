## Zadanie 1
Pobraæ z modu³u sklearn.datasets zbiór diabetes (load_diabetes). Nastêpnie dla ka¿dej zmiennej narysowaæ wykres rozrzutu wraz z dopasowan¹ lini¹ regrsji oraz wyœwietliæ podstawowe statystyki modelu: coef,std err,t, p-value. Kod ma dzi³aæ w pêtli oraz zadzia³aæ równie¿ gdy wybierzemy zbiór boston (load_boston)
***PodpowiedŸ***
do wyœwietlenia statystyk polecam u¿yæ modu³u statsmodels.formula.api

## Zadanie 2
Pobraæ z modu³u sklearn.datasets zbiór wine (load_wine). Zbiór podzieliæ na ucz¹cy, walidacyjny oraz testowy (proporcje 60% 20% 20%) . Nastêpnie nauczyæ na zbiorze ucz¹cym model regresji logistycznej oraz drzewa decyzyjnego. Dla obu modeli na zbiorze walidacyjnym wyliczyæ miarê F1 i na jej podstawie wybraæ lepiszy model. Na koñcu zrobiæ predykcjê wybranym modelem na zbiorze testowym i sprawdziæ statystyki precision, recall i f1 - te¿ wyœwietliæ jaki model zosta³ wybran.
***PodpowiedŸ***
Do podjêcia decyzji warto u¿yæ funkcji classification_report() z parametrem *output_dict=True*


