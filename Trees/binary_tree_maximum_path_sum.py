# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # we split the problem down. Every subtree must compute left subtree and right subtree and the path, left to right
        # Next, we compute if the left and right subtrees can update max by compute the path themselves
        # DFS based approach. We gonna visit every node only once O(N), if balanced tree it will be O(logN) best
        res = [root.val] # needs to be this as it will settle the global variable problem
        def dfs(node): # computes the subtree best path
            # Validate path currently
            if node is None: # Null node return 0
                return 0
            leftSubTree = max(dfs(node.left),0)
            rightSubTree = max(dfs(node.right), 0)
            # # Used clue
            # leftSubTree = max(leftSubTree, 0) # if left subtree sucks ass we dont take
            # rightSubTree = max(rightSubTree, 0) # if right subtree sucks ass we dont take
            # tmp = max(leftSubTree + node.val, rightSubTree + node.val, node.val, leftSubTree + rightSubTree + node.val, leftSubTree, rightSubTree)
            # check if need to take full path or none, since leftTmp and rightTmp is alr best possible, dont need to double account
            bestPath = node.val + leftSubTree + rightSubTree
            res[0] = max(res[0], bestPath ) # this line updates global max, for exp if bestPath is better than res's current path we change res to this
            return node.val + max(leftSubTree, rightSubTree) # Dont be confused, this updates the dfs recursive calls to take only left or right since its a path
        dfs(root)
        return res[0]