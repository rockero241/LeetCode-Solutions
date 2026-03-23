# Last updated: 3/23/2026, 12:22:35 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def maxPathSum(self, root: Optional[TreeNode]) -> int:
10        res = [root.val]
11
12        # return max path sum without split
13        def dfs(root):
14            if not root:
15                return 0
16
17            leftMax = dfs(root.left)
18            rightMax = dfs(root.right)
19            leftMax = max(leftMax, 0)
20            rightMax = max(rightMax, 0)
21
22            # Compute max path sum with split
23            res[0] = max(res[0], root.val + leftMax + rightMax)
24            return root.val + max(leftMax, rightMax)
25
26        dfs(root)
27        return res[0]