class Solution:
    # must use BFS. Which is implemented with a Queue
    # FIFO
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque() # python lib for queue
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node: # prevent None from appending to level
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: # level could be empty
                res.append(level)
        return res