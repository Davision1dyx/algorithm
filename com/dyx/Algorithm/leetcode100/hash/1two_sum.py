from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = dict()
        for i in range(len(nums)):
            if target - nums[i] in index:
                return [index[target - nums[i]], i]
            index[nums[i]] = i
        return []

s = Solution()
s.twoSum([2,5,5,11], 10)