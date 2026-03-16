# Last updated: 3/16/2026, 3:23:52 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
10        if not preorder or not inorder:
11            return None
12
13        root = TreeNode(preorder[0])
14        mid = inorder.index(preorder[0])
15
16        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
17        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
18
19        return root