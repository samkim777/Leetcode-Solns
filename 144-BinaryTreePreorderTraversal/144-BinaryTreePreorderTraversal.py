# Last updated: 4/9/2025, 11:08:22 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # root left right
        res = []
        def dfs(root):
            if not root:
                return None
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res