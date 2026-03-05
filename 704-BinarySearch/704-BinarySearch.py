# Last updated: 3/4/2026, 9:42:24 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4        while l <= r:
5            m = (l + r) // 2
6
7            if nums[m] < target:
8                l = m + 1
9            elif nums[m] > target:
10                r = m - 1
11            else:
12                return m
13                
14        return -1