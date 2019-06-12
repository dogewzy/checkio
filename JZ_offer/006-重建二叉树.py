"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
前序遍历的顺序为：根左右
中序遍历的顺序为：左根右

每次获取前序遍历的第一个数字，其在中序遍历中会把数组分成两个，就是其左子树和右子树

我对递归的掌握一直不太好，这里可以练习一下
先画一下递归的流程，确定函数的输入和结束条件：
f(12473568, 47215386)
取第一个列表的第一个数字作为根节点，然后以根节点把第二个列表分成两部分
上面函数会递归为下面两个，分别返回其左右子树的根节点
f(247,472)  f(4,4)  f(7,7)
f(3568,5386)  递归为 f(5,5) f(68,86), f(8,8)， f([],[])
遇到长度为1或者0时返回
"""
from JZ_offer.structure import BinaryTreeNode


def solution(front_iter, mid_iter):
    if set(front_iter) != set(mid_iter):
        raise AssertionError('序列不匹配')
    if len(front_iter) == 1:
        return BinaryTreeNode(front_iter[0])
    elif len(front_iter) == 0:
        return None
    else:
        root_value = front_iter[0]
        root = BinaryTreeNode(front_iter[0])
        mid_idx = mid_iter.index(root_value)
        left_mid, right_mid = mid_iter[:mid_idx], mid_iter[mid_idx+1:]
        left_front, right_front = front_iter[1:1+len(left_mid)], front_iter[1+len(left_mid):]
        root.left = solution(left_front, left_mid)
        root.right = solution(right_front, right_mid)
    return root


print(solution([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6]))
print('****************************')
print(solution([1,2,3,4,5], [5,4,3,2,1]))
print('****************************')
print(solution([1,2,3,4,5], [1,2,3,4,5]))
print('****************************')
print(solution([1, 2, 4, 5, 3, 6, 7], [4, 2, 8, 1, 6, 3, 7]))