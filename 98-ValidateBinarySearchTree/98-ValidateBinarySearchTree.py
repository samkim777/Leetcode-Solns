# Last updated: 4/11/2025, 10:32:51 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Binary Search tree contains no duplicates
        # Left subtree must all have values less than current node
        # Right subtree must all have values greater than current node
        # Use DFS to recursively check nodes
        # Determine base case: Return value: if reached end of tree, return True
        # because returning false will be tricky to handle as it might mean the tree is not valid
        # States: the current node's left and right children must be less and greater 
        # respectively, so should keep their values
        # in this case easier to just define dfs function to handle states
        def dfs(root, left_val, right_val):
            if not root:
                return True
            if not (left_val < root.val < right_val):
                return False
            return dfs(root.left, left_val, root.val) and dfs(root.right, root.val, right_val)
        return dfs(root, float("-inf"), float("inf"))