# Last updated: 4/6/2025, 11:43:53 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # BST: Return minimum abs difference between two values
        # So the smallest difference between any two nodes
        # brute force: get all the values in an array, sort, and return 
        # difference between first 2: O(nlogn) time complexity
        # what if for each node, we have a min difference
        # and compare between current and child
        res = []
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        min_diff = float('inf')
        for i in range(1, len(res)):
            min_diff = min(min_diff, abs(res[i] - res[i - 1]))

        return min_diff
            