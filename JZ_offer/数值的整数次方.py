"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""


# 显然可以偷懒……
def solution(base, exponent):
    return base ** exponent


"""
但是这个明显不是考察的知识点啊，
假设exponent是偶数，那么结果其实等于base ** （exponent/2） 的平方，然后进行递归，这样做的计算量会少一点，可以吧n次乘法变成log2n次乘法
如果是奇数则稍加变化，结果等级 base **((exponent-1)/2)*base
虽然我觉得这种水平的优化解释器肯定做掉了
"""


def solution2(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent // 2 == 1:
        return solution(base, (exponent - 1) / 2) * base
    else:
        return solution(base, exponent / 2) ** 2
