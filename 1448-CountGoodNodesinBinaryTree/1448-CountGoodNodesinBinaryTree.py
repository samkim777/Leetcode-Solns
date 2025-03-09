// Last updated: 3/8/2025, 10:45:02 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Determine return value and state
        # Return value: 0 when we hit base case
        # Return value cannot be boolean because we're trying to return
        # number of good nodes, so boolean doesn't make sense
        # State? maximum value seen so far
        def dfs(root, max_val):
            if not root:
                return 0
            # Declare total var, this will be returned to keep track of number
            # of good nodes
            goods = 0
            # is the current node value greater than or equal to max seen so far?
            if root.val >= max_val:
                goods += 1
                max_val = root.val
            
            # Traverse left and right nodes
            goods += dfs(root.left, max_val)
            goods += dfs(root.right, max_val)
            # Return this variable to keep track of number of good nodes
            return goods
        return dfs(root, float('-inf'))