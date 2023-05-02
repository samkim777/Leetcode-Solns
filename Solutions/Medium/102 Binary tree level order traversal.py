# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Basically implement a BFS
        res = []
        queue = collections.deque() 
        queue.append(root)
        while queue:
            level = []
            qlen = len(queue)
            for i in range(qlen):
                curNode = queue.popleft()
                if curNode:
                    level.append(curNode.val)
                    queue.append(curNode.left)
                    queue.append(curNode.right)
            if level:
                res.append(level)
        return res                
