from collections import deque


class BinaryTree:
    def __init__(self, val: int):
        self.val:int = val
        self.left:BinaryTree | None = None
        self.right:BinaryTree | None = None

# 初始化
n1 = BinaryTree(1)
n2 = BinaryTree(2)
n3 = BinaryTree(3)
n4 = BinaryTree(4)
n5 = BinaryTree(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
# 插入删除节点
# 插入
p = BinaryTree(0)
n2.right = p
p.left = n5
# 删除
n2.right = n5#(p.left)

# 使用一个队列，先进先出，完成二叉树的层序遍历
# 广度优先遍历。 bfs
def level_order(root: BinaryTree) -> list:
    res: list = []
    queue: deque[BinaryTree] = deque()
    queue.append(root)
    while queue:
        node: BinaryTree = queue.popleft()
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res
print(level_order(n1))

# 深度优先遍历  dfs
n3.left = BinaryTree(6)
n3.right = BinaryTree(7)

print("pre_order_recursive")
def pre_order_recursive(root: BinaryTree):
    if root is None:
        return
    print(root.val)
    pre_order_recursive(root.left)
    pre_order_recursive(root.right)
pre_order_recursive(n1)

print("\npre_order_stack")
def pre_order_stack(root: BinaryTree):
    if root is None:
        return
    stack :list[BinaryTree] = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
pre_order_stack(n1)

print("\nin_order_recursive")
def in_order_recursive(root: BinaryTree):
    if root is None:
        return
    in_order_recursive(root.left)
    print(root.val)
    in_order_recursive(root.right)
in_order_recursive(n1)

print("\nin_order_stack")
def in_order_stack(root: BinaryTree):
    if root is None:
        return
    stack :list[BinaryTree] = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val)
        current = current.right
in_order_stack(n1)

print("\npost_order_recursive")
def post_order_recursive(root: BinaryTree):
    if root is None:
        return
    post_order_recursive(root.left)
    post_order_recursive(root.right)
    print(root.val)
post_order_recursive(n1)

print("\npost_order_stack")
def post_order_stack(root: BinaryTree):
    if root is None:
        return
    res = []
    stack: list[BinaryTree] = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    res.reverse()
    print(res)
post_order_stack(n1)
