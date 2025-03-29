class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        pre_max = 0
        suf_max = 0
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])

            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans

s = Solution()
a = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(a))
b = [4,2,0,3,2,5]
print(s.trap(b))
