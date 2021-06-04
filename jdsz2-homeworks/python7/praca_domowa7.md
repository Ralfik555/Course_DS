## Zadanie 1
Z biblioteki sklearn.datastets pobraæ zbiór digits i podzieli na treningowy i testowy w stosunku 70-30. Nastêpnie utworzyæ na zbiorze treningowym model SVM metod¹ OneVsRest z wybranym przez siebie kernelem. Nastêpnie zwizualizowaæ na wykresie dwuwymiarowym zbiór testowy korzystaj¹c z tsne. Punkty odpowiadaj¹ce ka¿dej cyfrze powinny byæ namalowane na wykresie innym kolorem, ponadto nale¿y narysowaæ legendê z której dowiemy siê jaki kolor jak¹ cyfrê reprezentuje. Dodatkowo nanieœæ znaczniki x na punkty, które by³y b³êdnie sklasyfikowane wg modelu SVM.

*Dla chêtnych:*
Wizualizacja w 3D

## Zadanie 2

W katalogu "7_Bayes" znajduje siê plik "test.csv". Jest to plik bardzo podobny w strukturze do "train.csv" ale nie zawiera naszego "target variable" czyli informacji o tym kto prze¿y³ a kto nie.
Plik "test.csv zosta³ przygotowany przez twórców konkursu i zawiera informacje o pasa¿erach którzy nie wystêpuj¹ w pliku "train.csv". Nale¿y dokonaæ predykcji dla wszystkich wierszy i stworzyæ plik z rezultatem o strukturze podobnej do pliku "gender_submission.csv".
W pliku "gender_submission.csv" zak³adamy prosty model: ka¿da  ka¿da kobieta prze¿y³a a ka¿dy mê¿czyzna nie.
Oczywiœcie my chcemy u¿yæ  modelu który wytrenowaliœmy. Bazuje on na du¿o wiêkszej liczbie featere'ów i liczymy na lepszy wyniki ni¿ prosty model oparty o p³eæ.

Zadanie polega wiêc na stworzeniu pliku analogicznego do "gender_submission.csv" ale zawieraj¹cego predykcjê z waszego modelu zrobionego na zajêciach. Uzyskany plik wyœlijcie na stronê Kaggle i pochwalcie siê na Slacku jaki macie wynik. Równe¿ napiszcie wynik w pliku z kodem.