import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnistDir = 'C://data//mnist//'

mnist=input_data.read_data_sets(mnistDir, one_hot=True)

x1, y1 = mnist.train.next_batch(10)
print(x1.shape)
print(np.reshape(x1, [-1, 28, 28, 1]).shape)

tf.reset_default_graph()

#dodawanie szumu do zdjec
def addNoiseToImages(images, noiseStrengh = 0.1):
    imgsShape = images.shape
    noise = np.random.normal(0,noiseStrengh,imgsShape[0]*imgsShape[1]).reshape(imgsShape[0],imgsShape[1])
    imgsNoised = np.add(images, noise)
    return imgsNoised

#wyswietlanie pomocnicze
num = 1
X=mnist.test.images[:num]
X_Noised = addNoiseToImages(X, 0.2)
it = 1
for img in X_Noised:
    plt.subplot(num, 1, it)
    plt.imshow(img.reshape(28,28))
    it+=1
    plt.show()

tf.reset_default_graph()

#parametry warstw
num_inputs=784    #28x28 pixels
num_hid1=392
num_hid2=196
num_hid3=num_hid1
num_output=num_inputs
lr=0.01
actf=tf.nn.relu

#definicja warstw
X=tf.placeholder(tf.float32,shape=[None,num_inputs])
Xnoised=tf.placeholder(tf.float32,shape=[None,num_inputs])
initializer=tf.variance_scaling_initializer()

w1=tf.Variable(initializer([num_inputs,num_hid1]),dtype=tf.float32)
w2=tf.Variable(initializer([num_hid1,num_hid2]),dtype=tf.float32)
w3=tf.Variable(initializer([num_hid2,num_hid3]),dtype=tf.float32)
w4=tf.Variable(initializer([num_hid3,num_output]),dtype=tf.float32)

b1=tf.Variable(tf.zeros(num_hid1))
b2=tf.Variable(tf.zeros(num_hid2))
b3=tf.Variable(tf.zeros(num_hid3))
b4=tf.Variable(tf.zeros(num_output))

hid_layer1=actf(tf.matmul(Xnoised,w1)+b1)
hid_layer2=actf(tf.matmul(hid_layer1,w2)+b2)
hid_layer3=actf(tf.matmul(hid_layer2,w3)+b3)
output_layer=actf(tf.matmul(hid_layer3,w4)+b4)

#liczenie bledu
loss=tf.reduce_mean(tf.square(output_layer-X))

#optymalizacja
optimizer=tf.train.AdamOptimizer(lr)
train=optimizer.minimize(loss)

init=tf.global_variables_initializer()

#parametry uczenia
num_epoch=5
batch_size=150
num_test_images=5

#uruchomienie sesji
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(num_epoch):
        
        num_batches=mnist.train.num_examples//batch_size
        for iteration in range(num_batches):
            X_batch,y_batch=mnist.train.next_batch(batch_size)
            X_batchNoised = addNoiseToImages(X_batch, 0.3)
            sess.run(train,feed_dict={X:X_batch, Xnoised:X_batchNoised})
            
        train_loss=loss.eval(feed_dict={X:X_batch, Xnoised:X_batchNoised})
        print("epoch {} loss {}".format(epoch,train_loss))
        
    test = mnist.test.images[:num_test_images]
    testNoised = addNoiseToImages(test, 0.3)
    results=output_layer.eval(feed_dict={Xnoised:testNoised})
    
    #wyswietlenie reszultatow
    f,a=plt.subplots(3,5,figsize=(40,8))
    for i in range(num_test_images):
        a[0][i].imshow(np.reshape(test[i],(28,28)))
        a[1][i].imshow(np.reshape(testNoised[i],(28,28)))
        a[2][i].imshow(np.reshape(results[i],(28,28)))
    plt.show()