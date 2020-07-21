# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 求积分图.py
@CreateTime: 2020/7/20 17:57
'''
import numpy as np

def jifentu(img):
    jf_img =np.array(img)
    for m in range(1,jf_img.shape[0]):
        # 求出第一列积分图
        jf_img[m][0] += jf_img[m-1][0]
    for n in range(1,jf_img.shape[1]):
        # 求出第一行积分图
        jf_img[0][n] += jf_img[0][n-1]
    for m in range(1, jf_img.shape[0]):
        for n in range(1, jf_img.shape[1]):
            jf_img[m][n] += jf_img[m-1][n]+jf_img[m][n-1]-jf_img[m-1][n-1]
    return jf_img

if __name__ == '__main__':
    img = np.ones((50,50))
    print(jifentu(img))