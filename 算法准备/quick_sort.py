# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: quick_sort.py
@CreateTime: 2020/6/16 21:45
'''
# 思路:
'''
1. 如果开始大于等于结束，则退出
2. alist需要一直全部传入，保证整体修改
3. 建立mid_num 
'''
def quick_sort(alist,start,end):
    if start >= end: return
    # 左右指针赋值
    left ,right= start, end
    mid_num = alist[start]
    while left < right:
        while left < right and mid_num < alist[right]:
            right -=1
        # 到这里说明比right小
        alist[left] = alist[right]
        while left < right and mid_num >= alist[left]:
            left +=1
        alist[right] = alist[left]
    alist[left] =mid_num
    # mid_num不需要被列入计算
    quick_sort(alist,start,left-1)
    quick_sort(alist,left+1,end)

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)
