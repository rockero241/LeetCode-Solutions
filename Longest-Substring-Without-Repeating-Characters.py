1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        charSet = set()
4        res = 0
5        l = 0
6
7        for r in range(len(s)):
8            while s[r] in charSet:
9                charSet.remove(s[l])
10                l += 1
11
12            charSet.add(s[r])
13            res = max(res, (r - l) + 1)
14
15        return res