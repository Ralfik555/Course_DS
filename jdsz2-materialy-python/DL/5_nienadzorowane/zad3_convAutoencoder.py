import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data 

from tensorflow.layers import conv2d
from tensorflow.layers import max_pooling2d
from tensorflow.layers import dense
from tensorflow.layers import flatten
from tensorflow.layers import conv2d_transpose


mnistDir = 'C://data//mnist//'
mnist=input_data.read_data_sets(mnistDir, one_hot=True)

tf.reset_default_graph()

#parametry warstw
num_inputs = 784
num_input_channel = 1
num_convDown1_feat = 16
num_convDown2_feat = 32
num_hid0_feat = 1568
num_hid1_feat = 3
num_hid2_feat = 1568
num_convUp1_feat = 16
num_convUp2_feat = 1
lr=0.01

#definicja warstw
X=tf.placeholder(tf.float32,shape=[None, num_inputs])

initializer=tf.variance_scaling_initializer()

r = tf.reshape(X, [-1, 28, 28, 1])

#encoder
convDown1 = conv2d(inputs=r, filters=num_convDown1_feat, kernel_size=[3, 3], padding="same", activation=tf.nn.relu) # Nx28x28x16
mp1 = max_pooling2d(inputs=convDown1, pool_size=[2, 2], strides=2) # Nx14x14x16
convDown2 = conv2d(inputs=mp1, filters=num_convDown2_feat, kernel_size=[3, 3], padding="same", activation=tf.nn.relu) # Nx14x14x32
mp2 = max_pooling2d(inputs=convDown2, pool_size=[2, 2], strides=2) # Nx7x7x32

flat = flatten(mp2) # Nx1568
hid1 = dense(flat, num_hid1_feat) # Nx512 << encoded pictures

#decoder
hid2 = dense(hid1, num_hid2_feat) # Nx1568
rUp = tf.reshape(hid2, [-1, 7, 7, 32]) # Nx7x7x632
convUp1 = conv2d_transpose(inputs=rUp, filters=num_convUp1_feat, kernel_size=[3, 3], padding="same", strides=2, activation=tf.nn.relu) # Nx14x14x16
convUp2 = conv2d_transpose(inputs=convUp1, filters=num_convUp2_feat, kernel_size=[3, 3], padding="same", strides=2, activation=tf.nn.relu) # Nx28x28x1 << decoded pictures

output_layer=tf.reshape(convUp2, [-1, 784])

#liczenie bledu
loss=tf.reduce_mean(tf.square(output_layer-X))

#optymalizacja
optimizer=tf.train.AdamOptimizer(lr)
train=optimizer.minimize(loss)

init=tf.global_variables_initializer()

#parametry uczenia
num_epoch=5
batch_size=150
num_test_images=10

#uruchomienie sesji
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(num_epoch):
        
        num_batches=mnist.train.num_examples//batch_size
        for iteration in range(num_batches):
            X_batch,y_batch=mnist.train.next_batch(batch_size)
            sess.run(train,feed_dict={X:X_batch})
            
        train_loss=loss.eval(feed_dict={X:X_batch})
        print("epoch {} loss {}".format(epoch,train_loss))
        
        
    results=output_layer.eval(feed_dict={X:mnist.test.images[:num_test_images]})
    
    #wyswietlenie reszultatow
    f,a=plt.subplots(2,10,figsize=(20,4))
    for i in range(num_test_images):
        a[0][i].imshow(np.reshape(mnist.test.images[i],(28,28)))
        a[1][i].imshow(np.reshape(results[i],(28,28)))
    plt.show()