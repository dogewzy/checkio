class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self._left = self._right = self.parent = self.position = None

    """
    先求出这棵树的总宽度和根节点的位置（正中间）
    底层叶子节点距离父节点的1，再往上是2,4,8……
    我们从顶往下算
    为什么不从底向上，因为这样还要判断其在父节点的哪一边，而且还得先遍历一遍
    """

    def __repr__(self):
        # 打印出来

        self.position = (2 ** (self.tree_depth - 1)) - 1
        level = {0: [self]}
        now_level = 0
        width = 2 ** self.tree_depth - 1

        every_lines = []
        while level[now_level]:
            this_line = ['_'] * width
            for node in level[now_level]:
                this_line[node.position] = str(node.value)
            every_lines.append(''.join(this_line))
            now_level += 1
            level[now_level] = [node for node in
                                sum([[node.left, node.right] for node in level[now_level - 1]], [])
                                if node]
            for node in level[now_level]:
                offset = 2 ** (self.tree_depth - now_level - 1)
                if node == node.parent.left:
                    node.position = node.parent.position - offset
                if node == node.parent.right:
                    node.position = node.parent.position + offset
        return '\n'.join(every_lines)

    def __bool__(self):
        return self.value is not None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        if node is not None:
            node.parent = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        if node is not None:
            node.parent = self

    @property
    def depth(self):
        # 当前节点的深度
        d = 0
        node = self
        while node.parent is not None:
            d += 1
            node = node.parent
        return d

    @property
    def root(self):
        root = self
        while root.parent:
            root = root.parent
        return root

    @property
    def tree_depth(self):
        # 整棵树的深度
        now_level = 0
        level = {0: [self]}
        while level[now_level]:
            now_level += 1
            level[now_level] = [node for node in
                                sum([[node.left, node.right] for node in level[now_level - 1]], [])
                                if node]
        return now_level

    def from_list(self, l):
        pass


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


if __name__ == '__main__':
    b = BinaryTreeNode(5)
    b.left = BinaryTreeNode(4)
    b.right = BinaryTreeNode(3)
    b.right.right = BinaryTreeNode(2)
    b.left.left = BinaryTreeNode(6)
    b.left.left.right = BinaryTreeNode(7)
    print(b)
