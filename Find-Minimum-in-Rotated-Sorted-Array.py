1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l, r = 0, len(nums) - 1
4        res = nums[0]
5
6        while l <= r:
7            if nums[l] < nums[r]:
8                res = min(res, nums[l])
9                break
10
11            m = (l + r) // 2
12            res = min(res, nums[m])
13
14            if nums[m] >= nums[l]: #why?
15                l = m + 1
16            else:
17                r = m - 1
18
19        return res