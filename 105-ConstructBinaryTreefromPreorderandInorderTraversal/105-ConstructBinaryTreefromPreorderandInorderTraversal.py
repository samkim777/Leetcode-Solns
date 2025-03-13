// Last updated: 3/12/2025, 9:57:14 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder is middle -> Left -> RIght
        # inorder is left -> middle - Right
        # The first element of preorder is always the root
        # the elements to the left of preorder's middle found inside
        # inorder are the left subtree, and right is right subtree
        # Recursively go through both trees to construct binary tree
        # time complexity of O(n), space O(n) [Recurse calls]

        # base case
        if not preorder or not inorder:
            return None
        tree = TreeNode(preorder[0])
        parent_index = inorder.index(preorder[0])

        tree.left = self.buildTree(preorder[1:parent_index + 1], inorder[:parent_index + 1])
        tree.right = self.buildTree(preorder[parent_index+1:], inorder[parent_index + 1:])

        return tree