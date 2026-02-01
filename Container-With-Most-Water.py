1class Solution:
2    def maxArea(self, heights: List[int]) -> int:
3        l, r = 0, len(heights) - 1
4        maxArea = 0
5
6        while l < r:
7            area = min(heights[l], heights[r]) * (r - l)
8            maxArea = max(area, maxArea)
9
10            if heights[l] < heights[r]:
11                l += 1
12
13            else:
14                r -= 1
15
16        return maxArea
17