# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: leetcode14.py
@CreateTime: 2020/7/16 9:30
'''



def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
# 递归的思路，当传入最后一个数字的时候，与之前的内容进行合并
    def backtrack(combination, next_digits):
        # 递归的退出条件，当模型到底了
        if len(next_digits) == 0:
            output.append(combination)
            # 用循环将每个需要添加的内容放到列表中
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    output = []
    if digits:
        backtrack("", digits)
    return output

if __name__ == '__main__':
    # OK
    print(letterCombinations('2345'))
