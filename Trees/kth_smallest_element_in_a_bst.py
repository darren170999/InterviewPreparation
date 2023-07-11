class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr and stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right 
            
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # guaranteed BST
        result = []
        
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)  # Traverse left subtree
            result.append(node.val)  # Visit current node
            inorder(node.right)  # Traverse right subtree
        
        inorder(root)  # Start traversal from the root
        
        print(result)
        return result[k-1]