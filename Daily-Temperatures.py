1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        res = [0] * len(temperatures)
4        stack = []
5
6        for i, temp in enumerate(temperatures):
7            while stack and temp > stack[-1][0]:
8                tempSet = stack.pop()
9                res[tempSet[1]] = (i - tempSet[1])
10            
11            stack.append([temp, i])
12
13        return res