# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 第一题.py
@CreateTime: 2020/7/17 20:04
'''

def output_same(listn):
    set1 = set() # 查询set速度比list快很多
    same_list = []
    for num in listn:
        if num in set1:
            same_list.append(num)
        else:
            set1.add(num)
    return set(same_list)

if __name__ == '__main__':
    l = [1,1,1,2,5,5,10]
    print(output_same(l))
