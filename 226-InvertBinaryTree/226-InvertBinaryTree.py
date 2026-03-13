# Last updated: 3/13/2026, 2:25:10 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
10        if not root:
11            return None
12
13        tmp = root.left
14        root.left = root.right
15        root.right = tmp
16
17        self.invertTree(root.left)
18        self.invertTree(root.right)
19
20        return root