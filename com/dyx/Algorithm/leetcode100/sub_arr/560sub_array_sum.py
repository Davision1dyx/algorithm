'''给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。'''
from collections import Counter


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        pre_map = Counter()
        # 因为是求子串的个数，所以直接以value为计数,key为前继元素和
        pre_map[0] = 1 # 因为 每个pre自己也可以为答案之一 pre - 0 = k
        pre = 0
        ans = 0
        # pre[i] - pre[i-1] = k
        for i in range(0, len(nums)):
            pre = pre + nums[i]
            if pre - k in pre_map:
                ans += pre_map[pre - k]
            pre_map[pre] += 1
        return ans


    # def subarraySum(self, nums: list[int], k: int) -> int:
    #     state = 0
    #     res = 0
    #     selected = []
    #     return self.back_track(state, nums, selected, k, 0, res)
    #
    # def back_track(self, state: int, choices: list[int], selected: list[int], tar: int, start: int, res: int) -> int:
    #     if state == tar and start != 0:
    #         res += 1
    #         return res
    #     for index, choice in enumerate(choices):
    #         if index != start and start != 0:
    #             continue
    #         if state > tar:
    #             continue
    #         if index in selected:
    #             continue
    #         state += choice
    #         selected.append(index)
    #         tmp = start
    #         start = index + 1
    #         res = self.back_track(state, choices, selected, tar, start, res)
    #         state -= choice
    #         selected.pop()
    #         start = tmp
    #     return res
nums0 = [1,-1,0]
k0 = 0
nums1 = [1,1,1]
k1 = 2
nums2 = [1,2,3]
k2 = 3
s = Solution()
print(s.subarraySum(nums0, k0))
print(s.subarraySum(nums1, k1))
print(s.subarraySum(nums2, k2))

