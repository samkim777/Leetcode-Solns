# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if either tree empty
        if not p and q or not q and p:
            return False
        # both empty
        if not p and not q:
            return True
        # check value at node, and recurse down left and right nodes
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)        