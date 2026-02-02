1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        count = dict()
4        res = 0
5        l = 0
6
7        for r in range(len(s)):
8            count[s[r]] = 1 + count.get(s[r], 0)
9
10            while (r - l + 1) - max(count.values()) > k:
11                count[s[l]] -= 1
12                l += 1
13
14            res = max(res, r - l + 1)
15
16        return res