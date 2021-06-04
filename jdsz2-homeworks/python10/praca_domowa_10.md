# Zadanie 1

Poprawiæ baseline_model z przyk³adu https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/overfit_and_underfit.ipynb#scrollTo=Ofn1AwDhx-Fe, tak by model siê tak bardzo nie przeucza³, czyli w kolejnych epokach byœmy nie obserwowali takiego wzrostu binary_crossentropy na zbiorze walidacyjnym. W tym celu mo¿emy manipulowaæ iloœci¹ warstw oraz neuronów, dodawaæ DropOut oraz regularyzacjê.
W pierwszej kolejnosci waszymi wynikami podzielcie siê z grup¹ na kana³ach grup projektowych. Sprawdzimy której grupie uda siê opracowaæ najlepszy model.

# Zadanie 2
- Pobraæ repozytorium z przyk³adami polskiego word2vec: https://github.com/Ermlab/pl-sentiment-analysis/tree/50d5e8d7f0383fc353ff0e26c4af34f256031218
- Zainstalowaæ wszystkie potrzebne paczki zawarte w pliku LSTM.py (paczkê many_stop_words nale¿y popraæ poprzez pip - nie conda ) 
- Pobraæ dataset, s³ownik jêzyka polskiego i wstêpnie przetrenowane modele tak jak jest to wskazane w pliku README.md z tego repozytorium i umieœciæ je we wskazanych lokalizacjach.
- skompilowaæ kod LSTM.py do momentu: ( dalej jest budowa modelu - trwa bardzo d³ugo):
```python
embedding_matrix = word2vec_model.wv.syn0
```
W ten sposób otrzymujemy dla wszystkich s³ów w s³owniku wektory 100 - wymiarowe. 
Zadanie polega na wybraniu 10 wybranych przez siebie s³ów i zwizualizowanie ich w przestrzeni 2 wymiarowej u¿ywaj¹c tsne.
**PodpowiedŸ:**
Indeksy wybranych s³ów mo¿na uzyskaæ w nastêpuj¹cy sposób:
```python
word2index = {token: token_index for token_index, token in enumerate(word2vec_model.index2word)} 
word2index['kot']
```