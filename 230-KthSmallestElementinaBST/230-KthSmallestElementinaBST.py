# Last updated: 3/15/2026, 11:58:49 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
10        stack = []
11        cur = root
12        
13        while cur or stack:
14            while cur:
15                stack.append(cur)
16                cur = cur.left
17
18            cur = stack.pop()
19            k -= 1
20
21            if k == 0:
22                return cur.val
23            cur = cur.right