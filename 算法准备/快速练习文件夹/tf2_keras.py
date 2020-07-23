# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: tf2_keras.py
@CreateTime: 2020/7/5 14:17
'''

import tensorflow.python.keras as keras
import tensorflow as tf

# 定义网络
model = keras.models.Sequential([
            keras.layers.Flatten(),
            keras.layers.Dense(100, activation=tf.nn.relu),
            keras.layers.Dense(10),
            keras.layers.Softmax()
        ])

# 模型配置
model.compile(optimizer=keras.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 模型训练
model.fit(train_data, train_label, epochs=num_epochs, batch_size=batch_size)

# 模型评估
model.evaluate(test_images, test_labels)

# 模型预测
model.predict(test)