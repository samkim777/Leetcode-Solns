// Last updated: 3/22/2025, 10:27:21 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Using the property of BST, we can use dfs to 
        # traverse the tree and insert while keeping with the condition
        # if what we want to insert is less than cur, left 
        # if greater, right
        # THe value does not exist already so we don't have to worry about that
        # return values for dfs: None
        # state for dfs: value trying to insert
        # O(n) time in worst case, O(n) space in worst
        if not root:
            return TreeNode(val)
        def dfs(root, val):
            if not root:
                root = TreeNode(val)
                return TreeNode(val)
            if root.val > val:
                root.left = dfs(root.left, val)
            else:
                root.right = dfs(root.right,val)
            return root
        dfs(root, val)
        return root