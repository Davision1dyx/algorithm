'''给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其总和大于等于 target 的长度最小的 子数组
[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 '''

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = len(nums) + 1
        ans = 0
        left, j = 0, 0
        for right, num in enumerate(nums):
            ans += num
            while ans >= target:
                res = min(res, right - left + 1)
                ans -= nums[left]
                left += 1
        return res if res != len(nums) + 1 else 0



    # def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    #     res = len(nums) + 1
    #     ans = 0
    #     i, j = 0, 0
    #     while i < len(nums):
    #         if ans >= target:
    #             res = min(res, j - i)
    #             ans -= nums[i]
    #             i += 1
    #             continue
    #         if j <= len(nums) - 1:
    #             ans += nums[j]
    #             j += 1
    #         elif ans < target:
    #             ans -= nums[i]
    #             i += 1
    #     return res if res != len(nums) + 1 else 0

tar1 = 11
nums1 = [1,2,3,4,5]
tar2 = 4
nums2 = [1,4,4]
tar3 = 11
nums3 = [1,1,1,1,1,1,1,1]

s = Solution()
print(s.minSubArrayLen(tar1, nums1))
print(s.minSubArrayLen(tar2, nums2))
print(s.minSubArrayLen(tar3, nums3))