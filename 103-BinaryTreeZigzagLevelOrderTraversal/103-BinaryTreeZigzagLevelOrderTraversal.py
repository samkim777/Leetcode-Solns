# Last updated: 5/27/2025, 11:40:24 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        bLeftToRight = True
        while queue:
            level = len(queue)
            cur = deque()
            for _ in range(level):
                curr = queue.popleft()

                if bLeftToRight:
                    cur.appendleft(curr.val)
                else:
                    cur.append(curr.val)
                
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            res.append(list(cur))
            bLeftToRight = not bLeftToRight
        return res