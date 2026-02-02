1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if not t:
4            return ""
5
6        window = dict()
7        countT = Counter(t)
8        have, need = 0, len(countT)
9        res, resLen = [-1, -1], float("infinity")
10
11        l = 0
12        for r in range(len(s)):
13            c = s[r]
14            window[c] = 1 + window.get(c, 0)
15
16            if c in countT and window[c] == countT[c]:
17                have += 1
18
19            while have == need:
20                # update result
21                if (r - l + 1) < resLen:
22                    res = [l, r]
23                    resLen = (r - l + 1)
24                # pop from the left
25                window[s[l]] -= 1
26                if s[l] in countT and window[s[l]] < countT[s[l]]:
27                    have -= 1
28                l += 1
29
30
31        l, r = res
32        return s[l:r+1] if resLen != float("infinity") else ""
33