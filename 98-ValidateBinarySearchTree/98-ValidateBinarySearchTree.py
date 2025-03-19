# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lval, rval):
            if not root:
                return True
            if not (lval < root.val < rval):
                return False
            return (dfs(root.left, lval, root.val) and dfs(root.right, root.val,rval))
            
        return dfs(root, float('-inf'),float('inf'))