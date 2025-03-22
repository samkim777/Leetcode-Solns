// Last updated: 3/21/2025, 10:14:51 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # integers are immutable
        # meaning that if an integer is declared, even though it looks like
        # we're modifying it, we're actually creating new integer with 
        # a different id
        self.diameter = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.diameter = max(self.diameter, right + left)
            return 1 + max(left,right)
        dfs(root)
        return self.diameter