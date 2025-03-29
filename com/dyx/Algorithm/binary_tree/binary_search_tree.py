from idlelib.tree import TreeNode

from com.dyx.Algorithm.binary_tree.binary_tree import BinaryTree


class BinarySearchTree:
    def __init__(self, root:BinaryTree):
        self.root: BinaryTree | None = root

# 查找节点
    def search(self, num: int) -> TreeNode | None:
        cur = self.root
        while cur:
            if num < cur.val:
                cur = cur.left
            elif num > cur.val:
                cur = cur.right
            else:
                return cur
        return None

# 插入节点
    def insert(self, num: int):
        if self.root is None:
            self.root = BinaryTree(num)
            return
        cur = self.root
        pre: BinaryTree
        while cur:
            if num == cur.val:
                return
            if num < cur.val:
                cur = cur.left
            elif num > cur.val:
                cur = cur.right
            pre = cur
        if pre.val < num:
            pre.left = BinaryTree(num)
        else:
            pre.right = BinaryTree(num)
# 删除节点
    def remove(self, num: int):
        if self.root is None:
            return
        cur, pre = self.root, None
        while cur:
            if cur.val == num:
                break
            pre = cur
            if cur.val < num:
                cur = cur.left
            else:
                cur = cur.right
        # 如果不存在该节点，则直接返回
        if cur is None:
            return

        ## 子节点数量0或者1
        if cur.left is None or cur.right is None:
            child = cur.left or cur.right
            if cur != self.root:
                if cur == pre.left:
                    pre.left = child
                elif cur == pre.right:
                    pre.right = child
            else:
                self.root = child
        ## 度为2
        else:
            # 中序遍历右子树 获取后继节点
            tmp: BinaryTree = cur.right
            while tmp.left:
                tmp = tmp.left
            ## 迭代删除该后继节点
            self.remove(tmp.val)
            cur.val = tmp.val