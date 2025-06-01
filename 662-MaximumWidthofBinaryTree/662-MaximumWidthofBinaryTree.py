# Last updated: 5/31/2025, 11:14:37 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root,0)])
        res = 0

        while queue:
            lvl = len(queue)
            _, left = queue[0]
            right = -1

            for i in range(lvl):
                node, pos = queue.popleft()

                if i == lvl - 1:# reached the right most of our level
                    right = pos
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))
            res = max(res, right - left + 1)
        return res

