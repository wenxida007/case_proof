# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 股票一次买卖利润最高.py
@CreateTime: 2020/7/17 15:21
'''

def maxProfit(prices):
    n = len(prices)
    if n == 0: return 0 # 边界条件
    minprice = prices[0]
    max_benefit = 0
    for i in range(1, n):
        minprice = min(minprice, prices[i])
        # 记录每个位置和之前最小值的差额
        max_benefit = max(max_benefit, prices[i] - minprice)
    return max_benefit

if __name__ =='__main__':
    prices = [7,6,4,3,8]
    print(maxProfit(prices))

'''
作者：z1m
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/gu-piao-wen-ti-python3-c-by-z1m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''