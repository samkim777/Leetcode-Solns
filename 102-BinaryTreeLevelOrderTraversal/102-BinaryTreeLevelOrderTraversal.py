# Last updated: 5/25/2025, 10:50:13 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root])

        if not root:
            return []

        while queue:
            level = len(queue)
            curr = []
            for i in range(level):
                cur = queue.popleft()
                curr.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(curr)
        return res