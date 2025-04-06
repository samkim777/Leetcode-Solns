# Last updated: 4/5/2025, 10:04:33 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # The trick to this problem is to use the idea of levels
        # while utilizing dfs. We also note the fact that we could
        # just as easily use bfs to implement the solution as well
        res = []
        def dfs(root,level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            dfs(root.left,level + 1)
            dfs(root.right, level + 1)
        dfs(root,0)
        return res