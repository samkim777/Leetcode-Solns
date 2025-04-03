# Last updated: 4/2/2025, 11:04:30 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # path will be a string
        def dfs(root, path):
            if not root:
                return 0
            path += str(root.val)
            if not root.right and not root.left:
                return int(path)
            return dfs(root.left,path) + dfs(root.right, path)
        return dfs(root,"")