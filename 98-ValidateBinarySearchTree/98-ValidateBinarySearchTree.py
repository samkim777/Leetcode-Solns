// Last updated: 3/19/2025, 10:33:11 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # For each node, make sure that we are within the valid range
        # if not, return False
        # Note that we want to check all the tree nodes, so no premature return
        def dfs(root, l,r):
            if not root:
                return True
            if not (l < root.val < r):
                return False
            return dfs(root.left, l, root.val) and dfs(root.right, root.val, r)
        
        return dfs(root, float('-inf'), float('inf'))