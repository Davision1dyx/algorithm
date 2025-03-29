class MyHeap:
    def __init__(self):
        self.max_heap = []
    def left(self, i: int) -> int:
        return 2 * i + 1
    def right(self, i: int) -> int:
        return 2 * i + 2
    def parent(self, i: int) -> int:
        return (i - 1) // 2
    def peek(self) -> int:
        return self.max_heap[0]