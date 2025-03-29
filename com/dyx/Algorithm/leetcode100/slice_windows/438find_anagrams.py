class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        left = 0
        target = [0] * 26
        zi_mu = [0] * 26
        ans = []
        for c in p:
            target[ord(c) - ord("a")] += 1
        for right in range(len(s)):
            zi_mu[ord(s[right]) - ord("a")] += 1
            if right - left + 1< len(p):
                continue
            if  right - left + 1> len(p):
                zi_mu[ord(s[left]) - ord("a")] -= 1
                left += 1
            if tuple(zi_mu) == tuple(target):
                ans.append(left)
        return ans

s1 = "cbaebabacd"
p1 = "abc"
s2 = "abab"
p2 = "ab"
s = Solution()
print(s.findAnagrams(s1, p1))
print(s.findAnagrams(s2, p2))
