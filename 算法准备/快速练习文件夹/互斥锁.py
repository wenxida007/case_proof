# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 互斥锁.py
@CreateTime: 2020/7/16 8:51
'''

import threading


# 定义全局变量
g_num = 0

# 创建全局互斥锁
lock = threading.Lock()


# 循环一次给全局变量加1
def sum_num1():
    # 上锁
    # lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1

    print("sum1:", g_num)
    # 释放锁
    # lock.release()


# 循环一次给全局变量加1
def sum_num2():
    # 上锁
    # lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print("sum2:", g_num)
    # 释放锁
    # lock.release()


if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)
    # 启动线程
    first_thread.start()
    second_thread.start()
    while first_thread.is_alive() or second_thread.is_alive():
        continue
    print('last:',g_num)

