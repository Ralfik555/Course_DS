## Zadanie 1
Z biblioteki sklearn.datastets pobra� zbi�r digits i podzieli na treningowy i testowy w stosunku 70-30. Nast�pnie utworzy� na zbiorze treningowym model SVM metod� OneVsRest z wybranym przez siebie kernelem. Nast�pnie zwizualizowa� na wykresie dwuwymiarowym zbi�r testowy korzystaj�c z tsne. Punkty odpowiadaj�ce ka�dej cyfrze powinny by� namalowane na wykresie innym kolorem, ponadto nale�y narysowa� legend� z kt�rej dowiemy si� jaki kolor jak� cyfr� reprezentuje. Dodatkowo nanie�� znaczniki x na punkty, kt�re by�y b��dnie sklasyfikowane wg modelu SVM.

*Dla ch�tnych:*
Wizualizacja w 3D

## Zadanie 2

W katalogu "7_Bayes" znajduje si� plik "test.csv". Jest to plik bardzo podobny w strukturze do "train.csv" ale nie zawiera naszego "target variable" czyli informacji o tym kto prze�y� a kto nie.
Plik "test.csv zosta� przygotowany przez tw�rc�w konkursu i zawiera informacje o pasa�erach kt�rzy nie wyst�puj� w pliku "train.csv". Nale�y dokona� predykcji dla wszystkich wierszy i stworzy� plik z rezultatem o strukturze podobnej do pliku "gender_submission.csv".
W pliku "gender_submission.csv" zak�adamy prosty model: ka�da  ka�da kobieta prze�y�a a ka�dy m�czyzna nie.
Oczywi�cie my chcemy u�y�  modelu kt�ry wytrenowali�my. Bazuje on na du�o wi�kszej liczbie featere'�w i liczymy na lepszy wyniki ni� prosty model oparty o p�e�.

Zadanie polega wi�c na stworzeniu pliku analogicznego do "gender_submission.csv" ale zawieraj�cego predykcj� z waszego modelu zrobionego na zaj�ciach. Uzyskany plik wy�lijcie na stron� Kaggle i pochwalcie si� na Slacku jaki macie wynik. R�wne� napiszcie wynik w pliku z kodem.