# Last updated: 3/24/2026, 6:20:22 PM
1class Solution:
2    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
3        res = []
4
5        def dfs(i, cur, total):
6            if total == target:
7                res.append(cur.copy())
8                return
9
10            if i >= len(nums) or total > target:
11                return
12
13            cur.append(nums[i])
14            dfs(i, cur, total + nums[i])
15            cur.pop()
16            dfs(i + 1, cur, total)
17
18        dfs(0, [], 0)
19        return res