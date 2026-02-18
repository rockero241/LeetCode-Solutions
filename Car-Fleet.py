1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        res = []
4        pairs = [(p,s) for p,s in zip(position, speed)]
5
6        for p, s in sorted(pairs)[::-1]:
7            res.append((target - p) / s)
8            if len(res) >= 2 and res[-2] >= res[-1]:
9                res.pop()
10
11        return len(res)