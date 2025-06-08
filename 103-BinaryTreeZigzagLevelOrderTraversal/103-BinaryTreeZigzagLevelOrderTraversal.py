# Last updated: 6/7/2025, 10:08:09 PM
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
        ltr = True
        queue = deque([root])
        res = []

        while queue:
            lvl = len(queue)
            cur = []

            for _ in range(lvl):
                curr = queue.popleft()
                cur.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if not ltr:
                cur.reverse()
            ltr = not ltr
            res.append(cur)
        return res
                