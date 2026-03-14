# Last updated: 3/14/2026, 11:52:31 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
10        cur = root
11
12        while cur:
13            if p.val > cur.val and q.val > cur.val:
14                cur = cur.right
15            elif p.val < cur.val and q.val < cur.val:
16                cur = cur.left
17            else:
18                return cur