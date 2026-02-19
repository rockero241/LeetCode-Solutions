1from collections import Counter
2class Solution:
3    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
4        tally = [[] for _ in range(len(nums) + 1)]
5        res = []
6
7        count = Counter(nums)
8        for num, freq in count.items():
9            tally[freq].append(num)
10
11        for nlist in reversed(tally):
12            for num in nlist:
13                res.append(num)
14                k -= 1
15
16                if k == 0: 
17                    return res