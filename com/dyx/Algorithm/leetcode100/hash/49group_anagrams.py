import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)

        return list(mp.values())

    def groupAnagramss(self, strs: list[str]) -> list[list[str]]:
        mp = dict()
        for str in strs:
            count = [0] * 26
            for s in str:
                count[ord(s) - ord("a")] += 1
            if tuple(count) not in mp:
                mp[tuple(count)] = [str]
            else:
                mp[tuple(count)].append(str)
        return list(mp.values())






test = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
print(s.groupAnagramss(test))
test1 = ["", ""]
print(s.groupAnagramss(test1))
test2 = ["a"]
print(s.groupAnagramss(test2))