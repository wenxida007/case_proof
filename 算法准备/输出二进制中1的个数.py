# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 输出二进制中1的个数.py
@CreateTime: 2020/7/16 10:40
'''


N = int(input('请输入数字：'))
print("N:",bin(N))
binN = bin(N)[2:]
print('二进制效果：',binN)
count = binN.count('1')
print(count)

