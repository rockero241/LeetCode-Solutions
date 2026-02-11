1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l <= r:
6            m = (l + r) // 2
7            if target == nums[m]:
8                return m
9
10            # Left Portion
11            if nums[l] <= nums[m]:
12                if target < nums[l] or target > nums[m]:
13                    l = m + 1
14                else:
15                    r = m - 1
16
17            # Right Portion
18            else:
19                if target < nums[m] or target > nums[r]:
20                    r = m - 1
21                else:
22                    l = m + 1
23
24        return -1