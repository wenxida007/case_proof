# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 轮廓提取.py
@CreateTime: 2020/7/17 8:44
'''

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# 1 图像读取
# img = cv.imread('./data/tea.jpg')
img = cv.imread('./data/beijing.png')

imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# img_red = img[:,:,2]
# cv.imshow('img',img_red)
# cv.waitKey(0)
# 2 边缘检测
canny = cv.Canny(imgray,127,255,0)
# 3 轮廓提取
image, contours, hierarchy = cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
# 4 将轮廓绘制在图像上
img = cv.drawContours(img, contours, -1, (255,0,0), thickness=cv.FILLED)
# 5 图像显示
plt.imshow(img[:,:,::-1])
plt.xticks([]), plt.yticks([])
plt.show()
