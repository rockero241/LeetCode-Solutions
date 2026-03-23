# Last updated: 3/23/2026, 12:44:40 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
10        if not p and not q:
11            return True
12
13        if not p or not q or p.val != q.val:
14            return False
15
16        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)