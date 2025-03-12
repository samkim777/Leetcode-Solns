# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder is M -> L -> R
        # Inorder is L -> M -> R
        # First element of preoder is always node
        if not preorder or not inorder:
            return None
        tree = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # Find node inside inorder
        # Recurse
        tree.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        tree.right = self.buildTree(preorder[mid + 1:], inorder[mid+1:])
        return tree