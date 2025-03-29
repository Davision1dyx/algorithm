from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_sets = set(nums)
        longest = 0
        for num in num_sets:
            if num - 1 in num_sets:
                continue
            else:
                longest = max(self.longest_rec(num_sets, num, 0), longest)
        return longest

    def longest_rec(self, nums: set[int], num: int, longest: int) -> int:
        if num in nums:
            longest += self.longest_rec(nums, num + 1, longest)
            longest += 1
        return longest

s = Solution()
nums1 = [100,4,200,1,3,2]
print(s.longestConsecutive(nums1))
nums2 = [0,3,7,2,5,8,4,6,0,1]
print(s.longestConsecutive(nums2))
nums3 = [1,0,1,2]
print(s.longestConsecutive(nums3))