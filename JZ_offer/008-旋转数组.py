"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减序列的一个旋转，输出旋转数组的最小元素。

数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，

该数组的最小值为1。
"""


# 无论怎么样，最小的元素就在最大的元素后面,注意边界问题吧，这个时间复杂度和移动的距离有关
def solution(input):
    for idx, value in input[:-1]:
        if value > input[idx + 1]:
            return input[idx + 1]


# 分治法，最小的元素是两个有序数组的分割线，不停地取中间的元素和两边作比较，
# 但是要注意特殊情况，比如一开始就是有序的
# log n
def solutions2(input):
    front = 0
    end = len(input) - 1
    mid = len(input) // 2

    if input[front] <= input[end]:
        return input[front]
    while end - front > 1:
        if input[front] > input[mid]:
            end = mid
        elif input[front] <= input[mid]:
            front = mid
        mid = (end + front) // 2
    return input[end]

print(solutions2([1,2,3,4,5]))
