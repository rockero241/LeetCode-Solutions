1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l <= r:
6            m = (l + r) // 2
7
8            if nums[m] < target:
9                l = m + 1
10            elif nums[m] > target:
11                r = m - 1
12            else:
13                return m
14
15        return -1