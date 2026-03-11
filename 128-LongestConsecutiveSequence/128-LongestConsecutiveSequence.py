# Last updated: 3/11/2026, 5:14:12 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        numSet = set(nums)
4        longest = 0
5
6        for num in numSet:
7            if (num - 1) not in numSet:
8                count = 1
9                incr = num + 1
10
11                while incr in numSet:
12                    count += 1
13                    incr += 1
14
15                longest = max(longest, count)
16
17        return longest