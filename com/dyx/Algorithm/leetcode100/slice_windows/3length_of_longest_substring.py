from collections import Counter
'''给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        left = 0
        ans = 0
        for right, char in enumerate(s):
            count[char] += 1
            while count[char] > 1:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s = Solution()
print(s.lengthOfLongestSubstring(s1))
print(s.lengthOfLongestSubstring(s2))
print(s.lengthOfLongestSubstring(s3))