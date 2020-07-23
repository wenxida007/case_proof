# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 04_keras搭建线性模型.py
@CreateTime: 2020/7/21 15:44
'''



import tensorflow as tf
import numpy as np

# 1、定义一个线性回归模型
class Linear(tf.keras.Model):
    """自定义线性回归类
    """
    def __init__(self):
        super(Linear, self).__init__()
        # 实现一个线性回归层
        self.dense = tf.keras.layers.Dense(
            units=1,  # 线性回归和逻辑回归只有一个神经元
            activation=None,  # liner和lr没有激活函数
            kernel_initializer=tf.zeros_initializer(), #K初始化0
            bias_initializer=tf.zeros_initializer()  #  b也初始化0
        )

    def call(self, input):
        """调用模型的实现函数
        :param input: 模型输入值
        :return: 模型输出值
        """
        output = self.dense(input)
        return output


def linear_with_model():


    X_raw = np.array([[2013], [2014], [2015], [2016], [2017]], dtype=np.float32)
    y_raw = np.array([[12000], [14000], [15000], [16500], [17500]], dtype=np.float32)
    # 防止溢出，做归一化处理
    X = (X_raw - X_raw.min()) / (X_raw.max() - X_raw.min())
    y = (y_raw - y_raw.min()) / (y_raw.max() - y_raw.min())
    # [[0.]     [0.25]     [0.5]     [0.75]     [1.]]
    # [[0.]    [0.36363637]    [0.54545456]    [0.8181818]    [1.]]
    print(X,y)
    # 1、定义好数据类型以及参数类型
    X = tf.constant(X)
    y = tf.constant(y)
    # -------------------------------------------------------------------------------
    # tf定义常数的时候，需要定义二维的，一维数据会报错
    # X = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    # y = tf.constant([[10.0], [20.0]])

    epoch = 3000
    lr = 0.01
    # 2、进行训练步骤定义
    model = tf.keras.models.Sequential(tf.keras.layers.Dense(units=1, activation=None))
    optimizer = tf.keras.optimizers.SGD(learning_rate=lr)
    for i in range(epoch):
        with tf.GradientTape() as tape:
            y_pred = model(X)
            loss = 0.5 * tf.reduce_mean(tf.square(y_pred - y))  # squared_loss 最小二乘法损失

        # 梯度计算和更新
        grads = tape.gradient(loss, model.variables)
        optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))

    print("model.variables>>>:",model.variables) #W =array([[0.9613144]], dtype=float32)   B = =array([0.06590963], dtype=float32)  #epoch =3000 lr =0.01
    # print("model.layers>>>:",model.layers)
    # print("model.inputs>>>:",model.inputs)
    # print("model.outputs>>>:",model.outputs)
    # print("model.summary()>>>:",model.summary())

    return None


if __name__ == '__main__':
    linear_with_model()
