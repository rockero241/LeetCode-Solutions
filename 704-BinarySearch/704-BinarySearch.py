# Last updated: 3/2/2026, 4:39:24 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4        while l <= r:
5            m = (l + r) // 2
6            if nums[m] < target:
7                l = m + 1
8            elif nums[m] > target:
9                r = m - 1
10            else:
11                return m
12
13        return -1