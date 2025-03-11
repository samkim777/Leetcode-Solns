// Last updated: 3/10/2025, 10:38:41 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Isn't bfs better for this?
        # Using dfs, swap left and right node recursively
        # doesn't need return value
        # doesn't need state
        def dfs(root):
            # Base case
            if not root:
                return None
            # swap left and right
            dfs(root.right)
            dfs(root.left)
            temp = root.right
            root.right = root.left
            root.left = temp
        dfs(root)
        return root