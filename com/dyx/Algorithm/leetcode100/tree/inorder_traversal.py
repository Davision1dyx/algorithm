# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res: list[int] = []
        self.dfs(root, res)
        return res
    def dfs(self, root: TreeNode, res: list[int]):
        if root is None:
            return
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
