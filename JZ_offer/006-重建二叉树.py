"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
前序遍历的顺序为：根左右
中序遍历的顺序为：左根右

我对递归的掌握一直不太好，这里可以练习一下
递归的结束条件：
"""
from JZ_offer.structure import BinaryTreeNode

def solution(front_iter, mid_iter):
    root = BinaryTreeNode(None)
    def construct(node, front, mid):
        node.value = front[0]
        root_index = mid.index[node.value]
        print(root_index)
        left, right = mid[:root_index], mid[root_index+1:]
    return root


print(solution([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6]))