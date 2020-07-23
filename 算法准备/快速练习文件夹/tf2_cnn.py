# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: tf2_cnn.py
@CreateTime: 2020/7/3 21:52
'''
import tensorflow as tf
import tensorflow.python.keras as keras

X = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
y = tf.constant([[10.0], [20.0]])

# 1.构建线性模型
class Linear(keras.Model):
    def __init__(self):
        super(Linear, self).__init__()
        self.dense = keras.layers.Dense(
            units=1,
            activation=None,
            kernel_initializer=tf.zeros_initializer(),
            bias_initializer=tf.zeros_initializer()
        )

    def call(self, inputs, training=None, mask=None):
        ouput = self.dense(inputs)
        return ouput


l = Linear()
optimizer = keras.optimizers.SGD()
for i in range(1000):
    with tf.GradientTape() as tape:
        y_pre = l(X)
        loss = tf.reduce_mean(tf.square(y_pre - y))

    grads = tape.gradient(loss, l.variables)
    optimizer.apply_gradients(grads_and_vars=zip(grads, l.variables))

print(l)
print(l.variables)