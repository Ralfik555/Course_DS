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

#convolution
#conv2d(inputs=?, filters=?, kernel_size=[?, ?], padding="?", activation=?)

#optimizer
#tf.train.AdamOptimizer(?).minimize(?)

#reshaping
#tf.reshape(input, [-1, ?, ?, ?])
#######################################


#okreslic parametry warstw

#zdefiniowac warstwy

#liczenie bledu

#optymalizacja

#uruchomienie sesji

#trening

#wyswietlenie wyniku