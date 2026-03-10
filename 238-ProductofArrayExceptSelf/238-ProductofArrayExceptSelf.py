# Last updated: 3/10/2026, 3:44:37 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        res = [1] * len(nums)
4        pre = 1
5
6        for i in range(len(nums)):
7            res[i] = pre
8            pre *= nums[i]
9
10        post = 1
11        for i in range(len(nums) -1, -1, -1):
12            res[i] *= post
13            post *= nums[i]
14
15        return res