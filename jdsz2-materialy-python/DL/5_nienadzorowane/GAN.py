import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt

mnistDir = 'C://Users//Lenovo//Desktop//Krzysiakowe//jdsz2_dl_nienadzorowane//Deep-Autoencoder-using-Tensorflow//MNIST_data//'
mnist=input_data.read_data_sets(mnistDir, one_hot=True)

# ### Step 1. Setting hyperparameters for GAN
real_image_size = 784 #Only for MNIST dataset  28x28x1 = 784
g_hidden_size = 128 # This is how many nodes we use in a hidden layer in Generator
d_hidden_size = 128 # This is how many nodes we use in a hidden layer in Discriminator
learning_rate = 0.002 # Learning rate - parameter used for gradient descent
epochs = 100 # How many times do we run through whole network
z_size = 100 # The size of the latent vector which is the input to Generator
smooth = 0.1 # Smoothing value used at the end of Discriminator, this param helps classificator to converge better
batch_size = 100 # How many images we feed to the GAN at ones

def generator(inputs, hidden_size, reuse=False, alpha=0.01):
    
    with tf.variable_scope('generator', reuse=reuse):
        
        layer = tf.layers.dense(inputs, hidden_size, activation=None)
        layer = tf.maximum(layer*alpha, layer)
        
        logits = tf.layers.dense(layer, real_image_size, activation=None)
        output = tf.tanh(logits)
        
        return output

def discriminator(inputs, hidden_size, reuse=False, alpha=0.01):
    
    with tf.variable_scope('discriminator', reuse=reuse):
        
        layer = tf.layers.dense(inputs, hidden_size, activation=None)
        layer = tf.maximum(layer*alpha, layer)
        
        logits = tf.layers.dense(layer, 1, activation=None)
        output = tf.sigmoid(logits)
        
        return logits, output


# ### Step 3. Define GAN
# Inputs to our network
inputs = tf.placeholder(tf.float32, [None, real_image_size], name='real_img_input')
latent_input = tf.placeholder(tf.float32, [None, z_size], name='fake_img_input')


# #### Steo 3.2 Define Generator
#Generator outputs 
gen_out = generator(latent_input, g_hidden_size, reuse=False)


# #### Step 3.3 Define Discriminator
# Discriminator outputs for REAL images inputs
real_disc_logits, real_disc_output = discriminator(inputs, d_hidden_size, reuse=False)
# Discriminator outputs for FAKE images inputs
fake_disc_logits, fake_disc_output = discriminator(gen_out, d_hidden_size, reuse=True)


# #### Step 3.4 Define losses for Generator and Discriminator
#Loss for discriminator - Real images
dis_loss_real = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=real_disc_logits, 
                                                                       labels=tf.ones_like(real_disc_logits) * (1 - smooth)))
# Loss for discriminator - Fake images
dis_loss_fake = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=fake_disc_logits, 
                                                                       labels=tf.zeros_like(fake_disc_logits)))
#Total loss for Discriminator
dis_loss = dis_loss_real + dis_loss_fake
#Loss for Generator
gen_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=dis_loss_fake, 
                                                                       labels=tf.ones_like(dis_loss_fake)))

#Getting all trainable variables from GAN
trainable_vars = tf.trainable_variables()


# #### Step 3.5 Get lists of variables connected to Generator and Discriminator
#Separate vars used for generator and for discriminator
gen_vars = [var for var in trainable_vars if var.name.startswith('generator')]
dis_vars = [var for var in trainable_vars if var.name.startswith('discriminator')]


# #### Step 3.6 Define Generator and Discriminator Optimizers
#Optimize separatelly variables for Generator and for Discriminator
dis_optimizer = tf.train.AdamOptimizer(learning_rate).minimize(dis_loss, var_list=dis_vars)
gen_optimizer = tf.train.AdamOptimizer(learning_rate).minimize(gen_loss, var_list=gen_vars)


# ### Step 4. Train
session = tf.Session()
session.run(tf.global_variables_initializer())

total_loss = []
samples = []
losses = []
for i in range(epochs):    
    for ii in range(mnist.train.num_examples // batch_size):
        batch = mnist.train.next_batch(batch_size)
        
        batch_images = batch[0].reshape((batch_size, real_image_size))
        batch_images = batch_images * 2 - 1 # Normalize images
        
        latent_space = np.random.uniform(-1, 1, size=(batch_size, z_size))
        
        c_d, _ = session.run([dis_loss, dis_optimizer], feed_dict={inputs:batch_images, latent_input:latent_space})
        c_g, _ = session.run([gen_loss, gen_optimizer], feed_dict={latent_input:latent_space})
        
    
    losses.append((c_g, c_d))
    
    print('Epoch: {}/{}'.format(i, epochs), " | Generator loss: {:.4f}".format(c_g),
          " | Discriminator loss: {:.4f}".format(c_d))
    
    
    sample_z = np.random.uniform(-1, 1, size=(16, z_size))
    gen_samples = session.run(
                   generator(latent_input, hidden_size=g_hidden_size, reuse=True),
                   feed_dict={latent_input: sample_z})
    samples.append(gen_samples)

# fig, ax = plt.subplots()
# losses = np.array(losses)
# plt.plot(losses.T[0], label='Generator')
# plt.plot(losses.T[1], label='Discriminator')
# plt.title("Training Losses")
# plt.legend()


rows, cols = 10, 6
fig, axes = plt.subplots(figsize=(7,12), nrows=rows, ncols=cols, sharex=True, sharey=True)

for sample, ax_row in zip(samples[::int(len(samples)/rows)], axes):
    for img, ax in zip(sample[::int(len(sample)/cols)], ax_row):
        ax.imshow(img.reshape((28,28)), cmap='Greys_r')
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
plt.show()