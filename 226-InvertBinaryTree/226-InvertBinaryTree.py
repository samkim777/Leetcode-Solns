// Last updated: 3/11/2025, 10:39:04 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            # Base case
            if not root:
                return None
            # swap left and right
            dfs(root.right)
            dfs(root.left)
            temporary = root.right
            root.right = root.left
            root.left = temporary
        dfs(root)
        return root