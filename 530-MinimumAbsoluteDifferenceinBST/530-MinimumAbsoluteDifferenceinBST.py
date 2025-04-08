# Last updated: 4/7/2025, 10:19:23 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # use in-order: left, root, right to get values in ascending
        # compare each pair to get min diff
        res = []
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        minDiff = float("inf")
        dfs(root)
        for i in range(1,len(res)):
            minDiff = min(minDiff, abs(res[i]-res[i-1])) # index
        return minDiff