1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        ROWS, COLS = len(matrix), len(matrix[0])
4
5        top, bot = 0, ROWS - 1
6        while top <= bot:
7            row = (top + bot) // 2
8            if target > matrix[row][-1]:
9                top = row + 1
10            elif target < matrix[row][0]:
11                bot = row - 1
12            else:
13                break
14
15        if not (top <= bot):
16            return False
17
18        row = (top + bot) // 2
19        l, r = 0, COLS - 1
20
21        while l <= r:
22            m = (l + r) // 2
23            if target > matrix[row][m]:
24                l = m + 1
25            elif target < matrix[row][m]:
26                r = m - 1
27            else:
28                return True
29
30        return False