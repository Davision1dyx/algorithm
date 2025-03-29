'''在二叉树中搜索所有值为7的节点，请返回根节点到这些节点的路径'''
from com.dyx.Algorithm.binary_tree.binary_tree import BinaryTree

path = []
res = []

def preorder(node: BinaryTree):
    if node is None:
        return
    # 尝试
    path.append(node)
    if node.val == 7:
        return
    preorder(node.left)
    preorder(node.right)
    path.pop()
