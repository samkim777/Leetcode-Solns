# Last updated: 3/25/2025, 11:20:51 PM
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
        # To serialize a tree: Take a tree and make it into a list,
        # separated by commas
        # in-order? pre-order? whichever is the one where you go 
        # root left right
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val)) # What is root.val? int? obj?

            dfs(root.left)
            dfs(root.right)
            return res # need to return results array
        dfs(root)
        return ",".join(res)
        # So we end up like [1,2,3,4,5] etc
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # To deserialize, we'll recursively go through the results array data
        # constructed during serialize
        # does the tree val need to be ints? yeah Node.val is an int
        values = data.split(",")
        self.index = 0
        def dfs():
            if values[self.index] == "N":
                self.index += 1
                return None
            # How do I progress from here?? I'm not handling left and right
            # subtrees
            # remember that our data is preorder
            root = TreeNode(values[self.index])
            self.index += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
            


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))