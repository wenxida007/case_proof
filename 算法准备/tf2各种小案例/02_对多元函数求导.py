# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 对多元函数求导.py
@CreateTime: 2020/7/21 15:13
'''

import tensorflow.python as tf

# 2、多元函数求导
X = tf.constant([[1., 2.], [3., 4.]])
y = tf.constant([[1.], [2.]])
# 函数参数,初始化参数随便定义
w = tf.Variable(initial_value=[[1.], [2.]])
b = tf.Variable(initial_value=1.)

# 在这里可以执行自动求导
with tf.GradientTape() as tape:
    L = 0.5 * tf.reduce_sum(tf.square(tf.matmul(X, w) + b - y))

w_grad, b_grad = tape.gradient(L, [w, b])
print("".format(L.numpy(), w_grad.numpy(), b_grad.numpy()))

