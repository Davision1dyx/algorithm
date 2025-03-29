def find(nums: list[int], target: int) -> list[int]:
    return list(filter(lambda num: num == target, nums))

print(find([1, 2, 3, 4, 5], 5))
print(find([1, 3, 4, 2, 5], 2))


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: ListNode| None = None
