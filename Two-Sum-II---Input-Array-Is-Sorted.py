1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l, r = 0, len(numbers) - 1
4
5        while l < r:
6            twoSum = numbers[l] + numbers[r]
7
8            if twoSum < target:
9                l += 1
10            elif twoSum > target:
11                r -= 1
12            else:
13                return [l+1, r+1]