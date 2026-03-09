# Last updated: 3/9/2026, 7:37:34 AM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pairs = [[p,s] for p,s in zip(position, speed)]
4        res = []
5
6        for p, s in sorted(pairs)[::-1]:
7            res.append((target - p) / s)
8            if len(res) >= 2 and res[-1] <= res[-2]:
9                res.pop()
10
11        return len(res)