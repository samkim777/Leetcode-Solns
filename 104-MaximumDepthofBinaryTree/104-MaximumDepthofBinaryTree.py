# Last updated: 4/21/2025, 10:12:21 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if we use dfs,and compare the values returned from
        # recursing the left and right subtree, and take the maximum,
        # we should get the maximum depth of our tree
        # O(n) time complexity, O(h) avg space, O(n) worst space
        # if the tree looks a lil funky and is like a line
        def dfs(root):
            # base case, if none,just return 0
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            return 1 + max(left,right)
        return dfs(root)
