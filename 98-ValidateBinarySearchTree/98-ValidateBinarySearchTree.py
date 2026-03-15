# Last updated: 3/15/2026, 7:38:32 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def isValidBST(self, root: Optional[TreeNode]) -> bool:
10        def valid(node, left, right):
11            if not node:
12                return True
13            if not (left < node.val < right):
14                return False
15
16            return valid(node.left, left, node.val) and valid(
17                node.right, node.val, right)
18
19        return valid(root, float("-inf"), float("inf"))