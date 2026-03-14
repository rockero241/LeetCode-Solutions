# Last updated: 3/14/2026, 4:56:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
10        res = []
11
12        q = collections.deque()
13        q.append(root)
14
15        while q:
16            qLen = len(q)
17            level = []
18            for i in range(qLen):
19                node = q.popleft()
20                if node:
21                    level.append(node.val)
22                    q.append(node.left)
23                    q.append(node.right)
24            if level:
25                res.append(level)
26
27        return res