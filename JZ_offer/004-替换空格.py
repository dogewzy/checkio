"""
请实现一个函数，将一个字符串中的空格替换成“%20”。 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

We Are Happy

We%20Are%20Happy

python内置的replace应该是最好的，其他不使用动态数组的方法是先计算出总长度
"""


def solution(input):
    return input.replace(' ', '%20')


print(solution('we are happy'))
