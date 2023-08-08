# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Time O(n) for both serializing and deserializing
class Codec:
    # Many ways to do this problem
    # Pre-order Traversal in DFS
    # take root, then left then right and repeat if not null
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        # "1,2,N,N,3,4,N,N,5,N,N" -> eg of serialized
        ans = [] # store as ['1', '2'] then later .join()
        def dfs(node):
            if not node: # BASE CASE: return
                ans.append("N")
                return
            ans.append(str(node.val))# convert to string (just something you prefer)
            dfs(node.left) # each of this is settled by base case, so we just call this to see if we can append stuff to ans which is defined outside
            dfs(node.right)
        dfs(root)
        return ",".join(ans)

    def deserialize(self, data): # now we receive the data from serialized
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",") # we know its comma delimited
        self.i = 0 # self because we want it to be a member variable of this class and we want the variable to be globally accesible, init to 0 since we wanna start at 0
        def dfs(): # dont need pass anything as i is now global
            if vals[self.i] == "N": # BASE CASE
                self.i += 1 # we update the index
                return None
            # TreeNode here has int values so in this case, so we must convert string to int
            node = TreeNode(int(vals[self.i])) 
            self.i += 1# same increment
            node.left = dfs()
            node.right = dfs()
            return node # return root node we created
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))