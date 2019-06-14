"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

这是斐波那契数列的应用
直接递归超时了，可以倒着来
"""


def solution(number):
    if number in (1, 2):
        return number
    else:
        return solution(number - 1) + solution(number - 2)


def solution2(number):
    look_up = {1: 1, 2: 2}
    for i in range(1, number + 1):
        if i in look_up:
            continue
        else:
            look_up[i] = look_up[i - 1] + look_up[i - 2]
    return look_up[number]

print(solution2(100))