# Last updated: 6/10/2025, 8:57:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use dfs
        def dfs(root):
            if not root:
                return
            tmp = root.right
            root.right = root.left
            root.left = tmp
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return root