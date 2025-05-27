# Last updated: 5/26/2025, 11:29:08 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root])
        if not root:
            return []
        bShouldTraverseLTR = True
        while queue:
            curr = deque()
            lvls = len(queue)
            for _ in range(lvls):
                cur = queue.popleft()

                if bShouldTraverseLTR:
                    curr.append(cur.val)
                else:
                    curr.appendleft(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            bShouldTraverseLTR = not bShouldTraverseLTR
            res.append(list(curr))
        return res