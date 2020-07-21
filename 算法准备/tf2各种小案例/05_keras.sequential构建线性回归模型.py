# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 05_keras.sequential构建线性回归模型.py
@CreateTime: 2020/7/21 15:48
'''

import tensorflow as tf

def linear_with_model():
    # 原始数据房屋年份和价格
    # X = tf.constant([[2013], [2014], [2015], [2016], [2017]], dtype=tf.float32)
    # y = tf.constant([[12000], [14000], [15000], [16500], [17500]], dtype=tf.float32)
    # 这里直接定义归一化以后的数据
    # [[0.]     [0.25]     [0.5]     [0.75]     [1.]]
    # [[0.]    [0.36363637]    [0.54545456]    [0.8181818]    [1.]]
    X = tf.constant([[0.], [0.25], [0.5], [0.75], [1.]], dtype=tf.float32)
    y = tf.constant([[0.], [0.36363637], [0.54545456], [0.8181818], [1.]], dtype=tf.float32)
    epoch = 3000
    lr = 0.01
    # 2、进行训练步骤定义
    model = tf.keras.models.Sequential(tf.keras.layers.Dense(units=1)) # activation=None
    optimizer = tf.keras.optimizers.SGD(learning_rate=lr)
    for i in range(epoch):
        with tf.GradientTape() as tape:
            y_pred = model(X)
            loss = 0.5 * tf.reduce_mean(tf.square(y_pred - y))  # squared_loss 最小二乘法损失

        # 梯度计算和更新
        grads = tape.gradient(loss, model.variables)
        optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))

    print("model.variables>>>:",model.variables) #W =array([[0.92225486]], dtype=float32)   B = =array([0.08755819], dtype=float32)  #epoch =3000 lr =0.01
    # print("model.layers>>>:",model.layers)
    # print("model.inputs>>>:",model.inputs)
    # print("model.outputs>>>:",model.outputs)
    # print("model.summary()>>>:",model.summary())
    return None


if __name__ == '__main__':
    linear_with_model()
