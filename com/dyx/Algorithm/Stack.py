from com.dyx.Algorithm.LinkedList import ListNode

stack: list[int] = []
stack.append(1)
stack.append(3)
stack.append(2)
stack.append(5)
stack.append(4)

peek: int = stack[-1]
pop: int = stack.pop()
size: int = len(stack)
is_empty: bool = len(stack) == 0

class LinkedListStack:
    def __init__(self):
        self._size: int = 0
        self._peek: ListNode | None = None

    def size(self) -> int:
        return self._size
    def is_empty(self) -> bool:
        return self._size == 0
    def push(self, num: int):
        if self.is_empty():
            self._peek = ListNode(num)  ## 这里也可以直接链表尾节点为None
        else:
            a = ListNode(num)
            a.next = self._peek
            self._peek = a
        self._size += 1
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._peek.val
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            result = self._peek.val
            self._peek = self._peek.next
            self._size -= 1
            return result
    def to_list(self) -> list[int]:
        if self.is_empty():
            return []
        else:
            result: list[int] = [] * self._size
            tmp: ListNode = self._peek
            for i in range(self._size):
                result[i] = tmp.val
                tmp = tmp.next
            return  result


    def to_list_standard(self) -> list[int]:
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr