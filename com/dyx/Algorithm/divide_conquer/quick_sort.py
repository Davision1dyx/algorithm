def quick_sort(nums: list[int]):
    dfs(nums, 0, len(nums) - 1)


def dfs(nums: list[int], i: int, j: int):
    if i >= j:
        return
    l = i
    r = j
    while l < r:
        while l < r and nums[i] <= nums[r]:
            r -= 1
        while l < r and nums[i] > nums[l]:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    nums[i], nums[l] = nums[l], nums[i]

    dfs(nums, i, l - 1)
    dfs(nums, l + 1, j)


nums = [2,4,1,3,0,3,5]
quick_sort(nums)
print(f"quick_sort = {nums}")
