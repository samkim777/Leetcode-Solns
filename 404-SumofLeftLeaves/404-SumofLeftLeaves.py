# Last updated: 4/13/2025, 11:28:22 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Weird problem, but I think similar to the 
        # right view of tree, where we traverse each level 
        # to get the right most tree only
        lsum = 0
        def dfs(root, l):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if l else 0
            return dfs(root.left, True) + dfs(root.right, False)
        return dfs(root, False)