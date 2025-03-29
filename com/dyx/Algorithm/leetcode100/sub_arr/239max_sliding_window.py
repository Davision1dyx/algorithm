from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # 单调队列
        window = deque()
        ans = []
        # 滑动窗口公式
        for index, num in enumerate(nums):
        # 入
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(index)
        # 出
            if index - window[0] > k - 1:
                window.popleft()
        # 记录
            if index >= k - 1:
               ans.append(nums[window[0]])
        return ans
    # def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    #     # res = max(nums[i],nums[i-1],nums[i-1])
    #     res = []
    #     window = deque()
    #     for i in range(len(nums)):
    #         if i < k - 1:
    #             window.append(nums[i])
    #         else:
    #             window.append(nums[i])
    #             ans = window[0]
    #             for j in range(len(window)):
    #                 ans = max(ans, window[j])
    #             res.append(ans)
    #             window.popleft()
    #     return res

nums1 = [1,3,-1,-3,5,3,6,7]
nums2 = [1]
k1 = 3
k2 = 1
s = Solution()
print(s.maxSlidingWindow(nums1, k1))
print(s.maxSlidingWindow(nums2, k2))