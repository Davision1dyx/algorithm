class ArrayBinaryTree:
    def __init__(self, arr: list[int| None]):
        self._tree = list(arr)
    def size(self) -> int:
        return len(self._tree)
    def val(self, i: int) -> int| None:
        if i< 0 or i >= len(self._tree):
            return None
        return self._tree[i]
    def left(self, i: int) -> int| None:
        return i * 2 +1
    def right(self, i: int) -> int| None:
        return i* 2 + 2
    def parent(self, i: int) -> int| None:
        return (i-1) // 2
    def pre_order(self, i: int) -> int:
        print(self._tree[i])
        self.pre_order(self.left(i))
        self.pre_order(self.right(i))
