# Last updated: 4/2/2025, 10:54:49 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, sum):
            if not root:
                return 0
            sum += str(root.val)
            if not root.left and not root.right:
                return int(sum)
            return dfs(root.left, sum) + dfs(root.right, sum)
        return dfs(root,"")