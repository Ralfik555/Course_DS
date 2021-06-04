'''Trains a simple deep NN on the MNIST dataset.

Gets to 98.40% test accuracy after 20 epochs
(there is *a lot* of margin for parameter tuning).
2 seconds per epoch on a K520 GPU.
'''

from __future__ import print_function

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from keras import regularizers

# Definicja wielkości pojedyńczej "partii" dancyh. Więcej o batch_size:
# https://stats.stackexchange.com/questions/153531/what-is-batch-size-in-neural-network
batch_size = 128

# Liczba klas które będziemy przewidywać. Naszym zadaniem jest rozpoznanie cyfry na każdym obrazku,
# więc liczba klas=10
num_classes = 10

# Liczba epoch. Jedna epoka to "przepuszczenie" przez sieć wszystkich danych. Przykład dla danych w tym pliku:
# W danych treningowych znajduje się 60 000 obrazków, zastosowanie epochs = 20 spowoduje, że sieć zobaczy każdy znich
# 20 razy. Dla batch_size = 128 oznacza to że jedna epoka to 469 batch'y (ostatni batch ma tylko 96 obrazków bo
# 60000 = 468 * 128 + 96
epochs = 20

# Keras pozwala nam w taki prosty sposób pobrać i załadować dane dla wielu z dobrze znanych problemów. Rozpoznawanie
# cyfr MNIST jest jednym z nich.

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Shape naszych danych treningowych to (60000, 28, 28) czyli mamy 60000 obrazków, każdy jest kwadratem o boku 28px.
print("Po załadowaniu x_train.shape {}".format(x_train.shape))
print("Po załadowaniu y_train.shape {}".format(y_train.shape))
print("Po załadowaniu x_test.shape {}".format(x_test.shape))
print("Po załadowaniu y_test.shape {}".format(y_test.shape))

# Zmienamy kształt danych treningowych, tak aby zamiast 60000 "kwadratów" czyli tablic dwu-wymiarowych mieć 60000 tablic
# jednowymiarowych.
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# Zmienamy typ danych z Integer na Float czyli z liczb całkowitych na zmienno przecinkowe.
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Do tej pory nasze obrazki były reprezntowane przez liczby z zakresu od 0 do 255. Normalizujemy je dzieląc przez 255.
# Teraz ich zakres to od 0 do 1. Właśnie dlatego musieliśmy zmienić typ danych na Float.
x_train /= 255
x_test /= 255
print("Po przekształceniu x_train.shape {}".format(x_train.shape))
print("Po przekształceniu y_train.shape {}".format(y_train.shape))
print("Po przekształceniu x_test.shape {}".format(x_test.shape))
print("Po przekształceniu y_test.shape {}".format(y_test.shape))

print("Target features \"y_train\" dla pierwszego obrazka przed użyciem funkcji to_categorical() {}".format(y_train[0]))
print("Target features \"y_test\" dla pierwszego obrazka przed użyciem funkcji to_categorical() {}".format(y_test[0]))

# Zamieniamy nasze "target features" z liczby całkowitej na one-hot vector.
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

print("Target features \"y_train\" dla pierwszego obrazka po użyciu funkcji to_categorical() {}".format(y_train[0]))
print("Target features \"y_test\" dla pierwszego obrazka po użyciu funkcji to_categorical() {}".format(y_test[0]))


# Rozmiar warstwy sieci neuronowej
hidden_layer_size = 512

# Deklarujemy model keras. Na razie ta sieć neuronowa jest pusta.
model = Sequential()

# Dodajemy pierwszą warstwę do sieci neuronowej.
# input_shape=(784,) Ponieważ wejściem do sieci będą nasze dane, musimy zadeklarować jawnie jaki jest ich wymiar.
# kernel_regularizer=regularizers.l2(0.0002) definiujemy regularyzację L2
# activation='relu' jak activation function będziemy używać relu
model.add(Dense(hidden_layer_size, activation='relu', input_shape=(784,), kernel_regularizer=regularizers.l2(0.0002)))

# Dddajemy drugą warstwę do sieci. Ponieważ wejściem do niej jest wyjście z warstwy pierwszej nie musimy jawnie
# deklarować wymiaru "input_shape", model wie, że będzie on taki jak wielkość poprzedniej warstwy czyli
# "hidden_layer_size"
model.add(Dense(hidden_layer_size, activation='relu', kernel_regularizer=regularizers.l2(0.0002)))

# Na koniec dodajemy warstwę o wielkości takiej jakią mamy liczbę klas i dodajemy activation_function softmax. Softmax
# powoduje, że cokolwiek "wejdzie" do tej warstwy zostanie zamienione na wartości od 0 do 1 które dodatkowo sumują się
# do 1. Dzięki zastosowaniu categorical_crossentropy loss (czyli funkcji kosztu) wartości te będziemy mogli interpretować
# jako prawdopodbieństwo.
model.add(Dense(num_classes, activation='softmax'))

# Wypisujemy krótkie podsumowanie modelu.
model.summary()

# Tutaj definiujemy funkcję kosztu, optimizer (czyli konkretna metoda optymalizacji wykorzystująca backpropagation) oraz
# metrykę jaką będziemy oceniać nasz model, w tym przypadku accuracy.
model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

# Trenujemy model.
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))

print("history {}".format(history))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
