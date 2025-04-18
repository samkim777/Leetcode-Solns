# Last updated: 4/12/2025, 10:49:04 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None
            temp = root.left
            root.left = root.right
            root.right = temp
            dfs(root.left)
            dfs(root.right)
            return root
        return dfs(root)
