def insert_sort(nums: list[int]):
    for i in range(1, len(nums)):
        j = i - 1
        base = nums[i]
        while j >= 0 and nums[j] >= base:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = base
nums = [2, 4, 1, 3, 0, 3, 5]
insert_sort(nums)
print(f"insert_sort = {nums}")