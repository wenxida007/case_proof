# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: m个元素取出n个求组合.py
@CreateTime: 2020/7/20 17:12
'''

def jc(N):
    # 求阶乘
    multi = 1
    for i in range(N):
        multi *=(i+1)
    return multi

def C_zuhe(m,n):
    # 求C组合数的二进制
    if m >n and m<=0 and n<0:
        return False
    elif m == n or n==0 :
        return 1
    else:
        return bin(int(jc(m)/(jc(m-n)*jc(n))))

def count_last_zeros(b_num):
    # 求出二进制，反向数0的个数
    b = str(b_num[2:]) # 取0b1110 后面的的数字
    count = 0
    for i in reversed(b):
        if i == "0":
            count +=1
        else:
            break
    return count


if __name__ == '__main__':
    m,n = input('请输入m,n用空格隔开:').split(" ")
    print(count_last_zeros(C_zuhe(int(m),int(n))))