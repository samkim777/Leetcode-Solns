# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque([root])

        while queue:
            rightSide = None
            qlen = len(queue)
            for i in range(qlen):
                curNode = queue.popleft()
                if curNode:
                    rightSide = curNode
                    queue.append(curNode.left)
                    queue.append(curNode.right)
            if rightSide:
                res.append(rightSide.val)
        return res                