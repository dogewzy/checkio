"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

题解也就是缩小范围，它从右下角或者左上角开始比较，一次剔除一行
我看过题解之后依然想坚持自己的想法，就是比中间的值
一旦发现target在 m1, m2之间，那么它的值的范围就缩小到左下角和右上角的两个矩形中
"""


def solution(input, target):
    length = len(input)
    mid_values = [input[i][i] for i in range(length)]
    for idx, value in enumerate(mid_values):
        if target < value:
            if idx == 0:
                return False
            else:
                rect1 = [input[x][y] for x in range(idx) for y in range(idx, length)]
                rect2 = [input[x][y] for x in range(idx, length) for y in range(idx)]
                return target in rect1 + rect2

    return False


input = [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
    [6, 8, 11, 15]
]

print(solution(input, 7))