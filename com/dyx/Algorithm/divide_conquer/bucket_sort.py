def bucket_sort(nums: list[float]):
    # 初始化n/2个桶，每个桶两个元素
    k = len(nums) // 2
    buckets = [[] for _ in range(k)]
    for num in nums:
        i: int = int(num * k)
        buckets[i].append(num)
    i = 0
    for bucket in buckets:
        # 使用内置函数排序
        bucket.sort()
        for num in bucket:
            nums[i] = num
            i += 1

nums = [0.49, 0.96, 0.82, 0.15, 0.09, 0.57, 0.43, 0.91, 0.75, 0.15, 0.37]
bucket_sort(nums)
print(f"bucket_sort = {nums}")