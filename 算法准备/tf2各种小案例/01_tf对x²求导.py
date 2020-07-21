# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: tf对x²求导.py
@CreateTime: 2020/7/21 15:11
'''

# 完成自动求导的功能
import tensorflow.python as tf

x = tf.Variable(initial_value=3.)

with tf.GradientTape() as tape:
    y = tf.square(x)

# 使用tape中的gradient的方法计算导数
y_grad = tape.gradient(y, x)
print(y, y_grad)
