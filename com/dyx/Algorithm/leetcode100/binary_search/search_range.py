'''给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。'''

###  其实这个题可以转换为寻找 第一个>= target 的index1 和 第一个>= target + 1 的index2 - 1。  [index1, index2 - 1]

class Solution:

    def searchRange_standard(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1  # [left, right]  左闭右闭
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1 #[middle + 1, right]
            else:
                right = middle - 1 #[left, middle - 1]
        return left

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.searchRange_standard(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = self.searchRange_standard(nums, target + 1) -1
        return [left, right]

    # def searchRange(self, nums: list[int], target: int) -> list[int]:
    #     res = [len(nums), -1]
    #     self.binary_search(nums, 0, len(nums) - 1, target, res)
    #     if res[0] == len(nums):
    #         res[0] = -1
    #     return res

    # def binary_search(self, nums: list[int], start, end, target: int, res: list[int]):
    #     if end < start:
    #         return res
    #     middle = start + (end - start) // 2
    #     if nums[middle] > target:
    #         self.binary_search(nums, start, middle - 1, target, res)
    #     if nums[middle] < target:
    #         self.binary_search(nums, middle + 1, end, target, res)
    #     if nums[middle] == target:
    #         res[0] = min(res[0], middle)
    #         res[1] = max(res[1], middle)
    #         for i in range(middle + 1, len(nums)):
    #             if nums[i] == target:
    #                 res[1] = i
    #             else:
    #                 break
    #         for i in range(middle - 1, -1, -1):
    #             if nums[i] == target:
    #                 res[0] = i
    #             else:
    #                 break



nums1 = [1,1,2]
tar1 = 1
nums2 = [5,7,7,8,8,10]
tar2 = 6
nums3 = [2,2]
tar3 = 2
s = Solution()
print(s.searchRange(nums1, tar1))
print(s.searchRange(nums2, tar2))
print(s.searchRange(nums3, tar3))