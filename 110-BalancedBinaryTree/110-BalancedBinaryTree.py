// Last updated: 3/15/2025, 9:58:29 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            left_h = dfs(root.left)
            right_h = dfs(root.right)

            if abs(left_h - right_h) > 1:
                return -1
            if left_h == -1 or right_h == -1:
                return -1
            return max(left_h, right_h) + 1
        return dfs(root) != -1