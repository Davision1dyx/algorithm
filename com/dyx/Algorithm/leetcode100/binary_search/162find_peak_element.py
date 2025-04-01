'''峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。'''
from math import inf


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
    # 峰值： 大于左元素，小于右元素
        i = 0
        j = len(nums) - 1
        while i <= j:
            middle = i + (j - i) // 2

            if middle + 1 == len(nums):
                plus = -inf
            else:
                plus = nums[middle + 1]
            if middle - 1 == -1:
                sub = -inf
            else:
                sub = nums[middle - 1]
            if nums[middle] <= plus:
                i = middle + 1
            elif nums[middle] <= sub:
                j = middle - 1
            else:
                # nums[middle - 1] < nums[middle] > nums[middle + 1]
                return middle
        return -1

nums1 = [1,2,3,1]
nums2 = [1,2,1,3,5,6,4]
nums3 = [1]

s = Solution()
print(s.findPeakElement(nums1))
print(s.findPeakElement(nums2))
print(s.findPeakElement(nums3))