##使用分治思想实现二分搜索
def binary_search(nums: list[int], target: int, index1: int, index2: int) -> int:
    if index1 > index2:
        return -1
    mid = index1 + (index2 - index1) // 2
    if target < nums[mid]:
        return binary_search(nums, target, index1, mid - 1)
    if target > nums[mid]:
        return binary_search(nums, target, mid + 1, index2)
    if target == nums[mid]:
        return mid


def binary_search_recur(nums: list[int], target: int) -> int:
    return binary_search(nums, target, 0, len(nums) -1)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
print(f"binary_search_recur = {binary_search_recur(nums, target)}")

def binary_search_normal(nums: list[int], target: int) -> int:
    i = 0
    j = len(nums) -1
    while i < j:
        middle = i + (j - i) //2
        if nums[middle] > target:
            j = middle -1
        elif nums[middle] < target:
            i = middle + 1
        else:
            return middle
print(f"binary_search_normal = {binary_search_normal(nums, target)}")
