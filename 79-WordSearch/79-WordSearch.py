# Last updated: 3/27/2026, 2:54:14 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        ROWS, COLS = len(board), len(board[0])
4        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
5
6        def dfs(r, c, i):
7            if i == len(word):
8                return True
9            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
10                word[i] != board[r][c] or visited[r][c]):
11                return False
12
13            visited[r][c] = True
14            res = (dfs(r + 1, c, i + 1) or
15                   dfs(r - 1, c, i + 1) or
16                   dfs(r, c + 1, i + 1) or
17                   dfs(r, c - 1, i + 1))
18            visited[r][c] = False
19            return res
20
21        for r in range(ROWS):
22            for c in range(COLS):
23                if dfs(r, c, 0):
24                    return True
25        return False