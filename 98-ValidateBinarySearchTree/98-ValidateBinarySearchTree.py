# Last updated: 4/11/2025, 10:34:01 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # need to keep LEFT and RIGHT values for all nodes
        # parent needs to be SMALLER THAN ALL LEFT
        # parent needs to be GREATER THAN ALL RIGHT
        def dfs(root, l, r):
            if not root:
                return True
            if not (l < root.val < r):
                return False
            return dfs(root.left, l,root.val) and dfs(root.right,root.val,r)
        return dfs(root, float("-inf"), float("inf"))