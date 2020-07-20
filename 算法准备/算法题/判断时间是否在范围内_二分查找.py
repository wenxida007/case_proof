# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 第二题.py
@CreateTime: 2020/7/17 20:18
'''

def compare_high_low(time1,time2):
    # 比较两个数大小
    if time1[0]*100+time1[1]>=time2[0]*100+time2[1]:
        return True
    else:
        return False

def boolean_contains(list_times,tuple_time):
    max_length = len(list_times)
    right_cur = max_length
    left_cur = 0
    cur = 0
    while left_cur <right_cur:
        cur = (right_cur + left_cur) // 2
        # 如果找到刚好大于开始的就停
        if compare_high_low(tuple_time,list_times[cur][:2]):
            if left_cur == cur: break
            left_cur = cur
        else:
            if right_cur == cur: break
            right_cur = cur
    print(cur) # 二分查找最终确定位置
    # compare返回值如果是FALSE说明小于结尾，如果小于结束的位置，说明在里面
    # compare返回值如果是TURE说明大于结尾，不再里面
    return not compare_high_low(tuple_time,list_times[cur][2:]) and compare_high_low(tuple_time,list_times[cur][:2])

if __name__ == '__main__':
    list_times = [(5,0,16,20), (18,30,19,40), (20,10,20,30)]
    tuple_times = [(4,29),(5,30),(18,29),(18,35),(20,9),(20,29),(20,40)]
    answers = [0,1,0,1,0,1,0]
    for i,tuple_time in enumerate(tuple_times):
        print("num:{},answer:{},func:{}".format(i,answers[i],boolean_contains(list_times,tuple_time)))
