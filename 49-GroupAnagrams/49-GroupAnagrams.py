# Last updated: 3/9/2026, 7:42:16 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        res = defaultdict(list)
4        for word in strs:
5            sortedW = "".join(sorted(word))
6            res[sortedW].append(word)
7
8        return list(res.values())