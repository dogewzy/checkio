"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

把这个数转化成二进制然后计算1的数量
首先回忆补码的概念，正数的补码是其本身，负数的补码是符号位不变的情况下在其源码基础上全部取反。

这里有好多好多种方法

牛客网上的没有说清楚，一般指的就是32位的整数
"""


# 移位 最基础
def solution(number):
    count = 0
    while number:
        count += number % 2
        number = number // 2
    return count


# print(solution(-1))

#
"""
用与&运算,
我们考虑一个二进制数，假如是0，那就直接返回好了
不然它必然可以表示成   （1或0的序列，part1）1（n个0，n可以为0， part2）
我们把这个二进制数减一，可以发现part1不会变化，而后面的 1跟上n个0 会变成 0跟上n个1
那我们把减一之后的这个数和原数相与，part1不会改变，而后面的就全部变成0，总体结果来看就是少了一个1，
这就很妙了= =
"""


def solution2(number):
    count = 0
    while number:
        number &= number - 1
        count += 1
    return count


print(solution2(7))
# 如果整数范围确定，可以用查表法，先列出1-（2的八次方）的所有结果，然后把整数拆成n个八位
