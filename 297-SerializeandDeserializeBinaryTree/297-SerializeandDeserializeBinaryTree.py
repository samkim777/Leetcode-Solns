# Last updated: 3/24/2025, 8:48:37 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        values = data.split(",") # array of node values
        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(values[self.i]) # create node
            self.i += 1
            # construct left subtree
            node.left = dfs()
            # construct right ubstree
            node.right = dfs()
            return node # Return node to keep adding shit to it
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))