# Last updated: 3/9/2026, 7:50:14 PM
1from collections import Counter
2class Solution:
3    def isAnagram(self, s: str, t: str) -> bool:
4        count1 = Counter(s)
5        count2 = Counter(t)
6        return count1 == count2