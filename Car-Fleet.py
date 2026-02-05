1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pairs = [[P,S] for P,S in zip(position, speed)]
4        stack = []
5
6        for pair in sorted(pairs)[::-1]:
7            stack.append((target - pair[0]) / pair[1])
8            if len(stack) >= 2 and stack[-1] <= stack[-2]:
9                stack.pop()
10
11        return len(stack)