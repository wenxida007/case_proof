# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 03_线性回归拟合房价.py
@CreateTime: 2020/7/21 15:26
'''

import tensorflow as tf

 # 3、线性回归求解模型参数
def main():
    import numpy as np

    X_raw = np.array([2013, 2014, 2015, 2016, 2017], dtype=np.float32)
    y_raw = np.array([12000, 14000, 15000, 16500, 17500], dtype=np.float32)


    # 防止溢出，做归一化处理
    X = (X_raw - X_raw.min()) / (X_raw.max() - X_raw.min())
    y = (y_raw - y_raw.min()) / (y_raw.max() - y_raw.min())
    print(X, y)  #[0.   0.25 0.5  0.75 1.  ] [0.   0.36363637 0.54545456 0.8181818  1. ]

    # 1、定义好数据类型以及参数类型
    X = tf.constant(X)
    y = tf.constant(y)

    # 这里需要定义成float类型
    a = tf.Variable(initial_value=0.)
    b = tf.Variable(initial_value=0.)
    variables = [a, b]

    # 2、应用gradientTape进行迭代计算导数更新
    num_epoch = 1000
    # 定义优化器
    optimizer = tf.keras.optimizers.SGD(learning_rate=1e-2)
    for i in range(num_epoch):
        # gradientTape
        with tf.GradientTape() as tape:
            y_pred = a * X + b
            loss = 0.5 * tf.reduce_sum(tf.square(y_pred - y))

        # tensorflow自动求导
        grads = tape.gradient(loss, variables)

        # 进行梯度更新参数
        optimizer.apply_gradients(grads_and_vars=zip(grads, variables))

    print(a, b)  # 打印变量a和b
    # epoch =1000 lr =0.01
    # <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=0.97642905> <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=0.057532378>
    return None


if __name__ == '__main__':
    main()

