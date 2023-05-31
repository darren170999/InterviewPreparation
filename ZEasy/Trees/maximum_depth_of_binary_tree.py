# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Function starts by checking if node has no children
# If true return 1, if Node dont exists return 0
# same function is applied to both node's children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        max_temp_left = 0
        max_temp_right = 0

        if root.left:
            child_depth = self.maxDepth(root.left)
            max_temp_left = max(max_temp_left, child_depth)

        if root.right:
            child_depth = self.maxDepth(root.right)
            max_temp_right = max(max_temp_right, child_depth)

        return max(max_temp_left, max_temp_right) + 1
    