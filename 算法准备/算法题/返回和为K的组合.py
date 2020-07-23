# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 返回和为K的组合.py
@CreateTime: 2020/7/20 17:46
'''
#
# def pair(listm,k):
# 返回符合的下标
#     setm = set(listm)
#     for i,n in enumerate(listm):
#         if k - n in setm:return i,listm.index(k-n)
#     return None

def pair(listm,k):
    # 返回符合的全部数组
    setm = set(listm)
    output= []
    for n in listm:
        if k - n in setm:
            output.append((n,k-n))
            setm.remove(n)
    return output

if __name__ == '__main__':
    listm = [4,6,8,10,13,15]
    k = 23
    print(pair(listm,k))