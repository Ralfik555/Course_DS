# Zadanie 1

Poprawi� baseline_model z przyk�adu https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/overfit_and_underfit.ipynb#scrollTo=Ofn1AwDhx-Fe, tak by model si� tak bardzo nie przeucza�, czyli w kolejnych epokach by�my nie obserwowali takiego wzrostu binary_crossentropy na zbiorze walidacyjnym. W tym celu mo�emy manipulowa� ilo�ci� warstw oraz neuron�w, dodawa� DropOut oraz regularyzacj�.
W pierwszej kolejnosci waszymi wynikami podzielcie si� z grup� na kana�ach grup projektowych. Sprawdzimy kt�rej grupie uda si� opracowa� najlepszy model.

# Zadanie 2
- Pobra� repozytorium z przyk�adami polskiego word2vec: https://github.com/Ermlab/pl-sentiment-analysis/tree/50d5e8d7f0383fc353ff0e26c4af34f256031218
- Zainstalowa� wszystkie potrzebne paczki zawarte w pliku LSTM.py (paczk� many_stop_words nale�y popra� poprzez pip - nie conda ) 
- Pobra� dataset, s�ownik j�zyka polskiego i wst�pnie przetrenowane modele tak jak jest to wskazane w pliku README.md z tego repozytorium i umie�ci� je we wskazanych lokalizacjach.
- skompilowa� kod LSTM.py do momentu: ( dalej jest budowa modelu - trwa bardzo d�ugo):
```python
embedding_matrix = word2vec_model.wv.syn0
```
W ten spos�b otrzymujemy dla wszystkich s��w w s�owniku wektory 100 - wymiarowe. 
Zadanie polega na wybraniu 10 wybranych przez siebie s��w i zwizualizowanie ich w przestrzeni 2 wymiarowej u�ywaj�c tsne.
**Podpowied�:**
Indeksy wybranych s��w mo�na uzyska� w nast�puj�cy spos�b:
```python
word2index = {token: token_index for token_index, token in enumerate(word2vec_model.index2word)} 
word2index['kot']
```