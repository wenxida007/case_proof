# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 06_keras（完全体）搭建线性回归.py
@CreateTime: 2020/7/21 17:39
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
    epoch = 1000
    lr = 0.01
    # 2、进行训练步骤定义
    model = tf.keras.models.Sequential(tf.keras.layers.Dense(units=1)) # activation=None
    model.compile(optimizer= tf.keras.optimizers.Adam(learning_rate=lr),
                  loss=tf.keras.losses.MAE,
                  metrics=['accuracy'])
    model.fit(X,y,epochs=epoch) # 模型训练
    print("model.variables>>>:",model.variables) #W =array([[0.91038364]], dtype=float32)   B = array([0.09000011], dtype=float32)  #epoch =3000 lr =0.01
    print("loss,acc:",model.evaluate(X,y))  # 如果在compile里面定义了，那么每次训练会实时输出。
    return None


if __name__ == '__main__':
    linear_with_model()

