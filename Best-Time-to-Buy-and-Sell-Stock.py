1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        l, r = 0, len(prices) - 1
4        maxProfit = 0
5
6        for r in range(len(prices)):
7            profit = prices[r] - prices[l]
8            maxProfit = max(profit, maxProfit)
9
10            if prices[r] < prices[l]:
11                l = r
12                r += 1
13
14        return maxProfit