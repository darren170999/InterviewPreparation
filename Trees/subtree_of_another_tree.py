# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
       
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))
    def sameTree(self, s, t): 
        # we fail the check by returning false on any recursive call
        # we dont pass it we fail it to get correct answer
        if not s and not t: # check until reach nothing.
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return (self.sameTree(s.left, t.left) and
            self.sameTree(s.right, t.right))