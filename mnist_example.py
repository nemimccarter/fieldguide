# MNIST classifier

#import data
from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

def main(_):
	mnist = input_data.read_data_sets*FLAGS.data_dir, one_hot=True)

	# placeholder
	x = tf.placeholder(tf.float32, [None, 784])
	# weight
	W = tf.Variable(tf.zeros([784, 10]))
	# bias
	b = tf.Variable(tf.zeros([10]))
	#model
	y = tf.matmul(x, W) + b

	#Define loss (cross-entropy)  and optimizer
	y_ = tf.placeholder(tf.float32, [None, 10])
	# The raw formulation of cross-entropy,
	#   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.softmax(y)),
	#                                 reduction_indices=[1]))
	# can be numerically unstable, so here we use 
	# tf.nn.softmax_cross_entropy_with_logits on the raw
	# outputs of 'y', and then average across the batch.
	cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, y_))
	train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)d optimizer
	y_ = tf.placeholder(tf.float32, [None, 10])

	sess = tf.InteractiveSession()
	#Now we train
	tf.intialize_all_varaibles().run()
	for _ in range(1000):
		batch_xs, batch_ys = mnist.train.next_batch(100)
		sess.run(train_step, feed_dict={x: batch_xs, y_: batch _ys})

	# Testing model
	correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
	print(sess.run(accuracy, feed_dict={x: mnist.test.images,
																			y_: mnist.test.labels}))
