"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # map old nodes to new nodes
        # create a copy of every nodes visited
        oldToNew = {}
        if node is None:
            return None
        def dfs(node):
            if node in oldToNew: # if alr exists
                return oldToNew[node]
            newNode = Node(node.val) # creating new node
            oldToNew[node] = newNode # map old node to new node
            for neigh in node.neighbors:
                newNode.neighbors.append(dfs(neigh)) # append neighbor nodes to newly created nodes
                # Every original neighbor of node will trigger the recursion and once the OG node is 
                # found, then we will stop recursion.
            return newNode
        return dfs(node)