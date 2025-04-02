# Last updated: 4/1/2025, 11:14:22 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def dfs(root):
            if not root:
                return
            # in order-> left, root, right
            dfs(root.left)
            res.append(root)
            dfs(root.right)
        dfs(root)

        first , second = None, None
        for i in range(len(res) - 1):
            if res[i].val > res[i + 1].val:
                if not first: 
                    first = res[i]
                second = res[i+1]
        first.val, second.val = second.val, first.val
        return [result.val for result in res]
