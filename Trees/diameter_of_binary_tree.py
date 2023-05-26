class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0] # global maximum, the one we return
        def dfs(root): # checks for the height
            if not root: # rmb height of null root is -1
                return -1
            l = dfs(root.left)
            r = dfs(root.right)
            # if height is -1, none node, ans will not change
            # add +2 to left and right, just rmb
            # the rest just makes sense
            ans[0] = max(ans[0], 2+ l + r) 
            return 1 + max(l, r)
        # call it once before we return answer
        dfs(root)
        return ans[0]