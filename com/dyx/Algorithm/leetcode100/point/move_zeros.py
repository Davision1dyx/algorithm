from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[j] = nums[i]
            j += 1
        for i in range(j, len(nums)):
            nums[i] = 0

nums1 = [0,1,0,3,12]
nums2 = [0]
s = Solution()
s.moveZeroes(nums1)
print(nums1)
s.moveZeroes(nums2)
print(nums2)