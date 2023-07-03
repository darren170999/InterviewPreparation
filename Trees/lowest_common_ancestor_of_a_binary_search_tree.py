# start at root and check where p and q is
# right holds larger than root and left is smaller than root
# if one of them is the root, then root is potentially the LCA
# if one is in left sub tree and one is in right sub tree then root is LCA
# this way we only need to visit one node per level
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q:'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
