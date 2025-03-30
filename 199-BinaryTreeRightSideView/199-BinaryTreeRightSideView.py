# Last updated: 3/29/2025, 10:58:33 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # In simple terms, return the right most node val at each level
        # ooooh level similar to what I solved yesterday maybe
        # seems like we can use dfs for this
        # per level, add right most node val
        # Time complexity of O(h) on average where h is height of tree
        # worst case O(n) same for space
        res = []
        def dfs(root,level):
            # base case, if no node, return None
            if not root:
                return None
            # At each "level", add right most node val
            # maybe we can use the index of the int as "level"
            # so value at index 1 is level 1 right most value
            # and if already exists, continue traversing
            if level == len(res): # level 0, item = 0, we can add
                res.append(root.val)
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)
            return res # hmm
        dfs(root,0)
        return res