from sklearn.datasets import load_iris
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD,Adam
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import tensorflow as tf

encoder =  LabelEncoder()
iris = load_iris()
X = iris.data
y = iris.target
y1 = encoder.fit_transform(y)
Y = pd.get_dummies(y1).values

model = Sequential()
model.add(Dense(10,input_shape=(4,),activation='tanh'))
model.add(Dense(8,activation='tanh'))
model.add(Dense(6,activation='tanh'))
model.add(Dense(3,activation=tf.nn.softmax))

model.compile(Adam(lr=0.04),'categorical_crossentropy',metrics=['accuracy'])

model.summary()

model.fit(X,Y,epochs=100)
y_pred = model.predict(X)

