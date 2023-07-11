# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val): 
            # min_val is upper bound of left, max_val is lower bound of right
            if node is None:
                return True
            # check if bst constraints are violated
            if min_val is not None and node.val <= min_val:
                return False
            if max_val is not None and node.val >= max_val:
                return False
            # dfs is called to update the bounds of values
            left_valid = dfs(node.left, min_val, node.val)
            right_valid = dfs(node.right, node.val, max_val)
            # if either is false return false
            return left_valid and right_valid
        
        return dfs(root, None, None)