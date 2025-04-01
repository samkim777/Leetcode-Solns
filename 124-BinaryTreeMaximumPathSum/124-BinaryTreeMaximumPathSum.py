# Last updated: 3/31/2025, 11:08:42 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # If the value is negative, is there ever a case we'd like to 
        # add that number? No
        # So when the node value is negative, that path should not be taken
        # if node val negative, simply return max of left or right subtree val
        # else if positive, just add the current node to path sum
        # O(n) time complexity and O(h) avg space, O(n) worst space
        self.pathSum = float('-inf')
        def dfs(root):
            if not root:
                return 0
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)
            curMax = right + left + root.val
            self.pathSum = max(curMax, self.pathSum)
            return root.val + max(left,right)
        dfs(root)
        return self.pathSum