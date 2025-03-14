// Last updated: 3/13/2025, 10:20:57 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # No state or value to return
        def dfs(root):
            if not root:
                return
            temp = root.right
            root.right = root.left
            root.left = temp
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return root