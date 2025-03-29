class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            res = max(res, area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return res

height1 = [1,8,6,2,5,4,8,3,7]
height2 = [1,1]
s = Solution()
print(s.maxArea(height1))
print(s.maxArea(height2))

