1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        l, r = 1, max(piles)
4        res = r
5
6        while l <= r:
7            k = (l + r) // 2
8            hours = 0
9            for p in piles:
10                hours += math.ceil(p / k)
11
12            if hours <= h:
13                res = min(res, k)
14                r = k - 1
15            else:
16                l = k + 1
17
18        return res