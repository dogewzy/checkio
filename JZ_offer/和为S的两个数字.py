"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
"""

def solution(array, tsum):
    values = {}
    for i in array:
        if i in values:
            values[i][0] = True
        else:
            values[tsum-i] = [False, i*(tsum-i)]
    result = sorted([i for i in values.keys() if values[i][0] is True], key=lambda x: x*(tsum-x))
    if not result:
        return []
    return sorted([result[0], tsum-result[0]])


# 使用的更多的是左右夹逼法，因为是有序的，左指针右移是最小的增大，右指针左移是最小的变小
def solution2(array, tsum):
    if not array:
        return []
    p1, p2 = 0, len(array)-1
    while array[p1] + array[p2] != tsum:
        if p1 == p2:
            return []
        if array[p1] + array[p2] < tsum:
            p1 += 1
        else:
            p2 -= 1
    return [array[p1], array[p2]]

print(solution2([1,2,4,7,11,15],15))