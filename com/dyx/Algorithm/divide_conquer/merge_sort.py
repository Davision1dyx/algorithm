def merge_sort(nums: list[int]):
    dfs(nums, 0, len(nums) - 1)

def dfs(nums: list[int], l: int, r: int):
    if l >= r:
        return
    mid = l + (r - l) // 2
    dfs(nums, l, mid)
    dfs(nums, mid +1, r)
    merge(nums, l, mid, mid + 1,  r)

def merge(nums: list[int], l1: int, r1: int, l2: int, r2: int):
    tmp = []
    start = l1
    while l1 <= r1 and l2 <= r2:
        if nums[l1] > nums[l2]:
            tmp.append(nums[l2])
            l2 += 1
        else:
            tmp.append(nums[l1])
            l1 += 1
    while l1 <= r1:
        tmp.append(nums[l1])
        l1 += 1
    while l2 <= r2:
        tmp.append(nums[l2])
        l2 += 1
    for i in range(0, len(tmp)):
        nums[start + i] = tmp[i]

nums = [2, 4, 1, 3, 0, 3, 5]
merge_sort(nums)
print(f"merge_sort = {nums}")
