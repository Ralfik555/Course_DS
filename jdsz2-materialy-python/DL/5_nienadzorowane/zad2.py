import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


mnistDir = 'C://data//mnist//'

mnist=input_data.read_data_sets(mnistDir, one_hot=True)

x1, y1 = mnist.train.next_batch(10)
print(x1.shape)
print(np.reshape(x1, [-1, 28, 28, 1]).shape)
plt.imshow(np.reshape(mnist.test.images[0],(28,28)))
		
tf.reset_default_graph()

#Tips
#input to the model
#tf.placeholder(tf.float32,shape=[None,num_inputs])

#wights defining
#initializer=tf.variance_scaling_initializer()
#weights=tf.Variable(initializer([num_input_feat,num_output_feat]),dtype=tf.float32)
#biases=b1=tf.Variable(tf.zeros(num_output_feat))

#multipy
#tf.matmul()

#activation function
#tf.nn.relu()

#optimizer
#tf.train.AdamOptimizer(?).minimize(?)

#######################################

#okreslic parametry warstw

#zdefiniowac warstwy

#liczenie bledu

#optymalizacja

init=tf.global_variables_initializer()

#parametry uczenia

#uruchomienie sesji
with tf.Session() as sess:
    sess.run(init)
	
#trening

#wyswietlenie wyniku