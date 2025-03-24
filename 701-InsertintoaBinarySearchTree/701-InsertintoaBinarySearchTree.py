# Last updated: 3/23/2025, 9:27:28 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case: once we find position, insert node into tree
        # state: none
        # Edge case:
        if not root:
            return TreeNode(val)
        def dfs(root, val):
            if not root:
                return TreeNode(val)
            if val > root.val:
                root.right = dfs(root.right, val)
            else:
                root.left = dfs(root.left, val)
            return root
        dfs(root, val)
        return root
