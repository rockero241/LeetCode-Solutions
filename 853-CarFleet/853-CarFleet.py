# Last updated: 3/6/2026, 9:52:20 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pairs = [[p, s] for p,s in zip(position, speed)]
4        res = []
5
6        for p, s in sorted(pairs)[::-1]:
7            res.append((target - p) / s)
8            if len(res) >= 2 and res[-2] >= res[-1]:
9                res.pop()
10        
11        return len(res)