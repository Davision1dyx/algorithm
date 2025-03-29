'''给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        left = 0
        ans = 1
        for right, num in enumerate(nums):
            ans *= num
            while ans >= k:
                ans /= nums[left]
                left += 1
            res += right - left + 1
        return res

nums1 = [10,5,2,6]
k1 = 100
nums2 = [1,2,3]
k2 = 0
s = Solution()
print(s.numSubarrayProductLessThanK(nums1, k1))
print(s.numSubarrayProductLessThanK(nums2, k2))