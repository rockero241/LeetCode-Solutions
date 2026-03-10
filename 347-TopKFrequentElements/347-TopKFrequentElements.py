# Last updated: 3/9/2026, 8:17:59 PM
1from collections import Counter
2class Solution:
3    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
4        freq = [[] for _ in range(len(nums) +1)]
5        res = []
6
7        count = Counter(nums)
8        for num, numF in count.items():
9            freq[numF].append(num)
10
11        for nums in freq[::-1]:
12            for num in nums:
13                res.append(num)
14                k -= 1
15                
16                if k == 0:
17                    return res
18
19        return res