# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 返回满足和的数组.py
@CreateTime: 2020/7/20 17:46
'''

def pair(listm,k):
    setm = set(listm)
    for i,n in enumerate(listm):
        if k - n in setm:return i,listm.index(k-n)
    return None

if __name__ == '__main__':
    listm = [1,4,5,7,8,9,10]
    k = 9
    print(pair(listm,k))