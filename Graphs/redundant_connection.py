class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # need use Union Find by rank to find better O(n) solution O(n^2) will also solve in time
        # since there are more than one ways to get to a particular node,
        # A redundant connection is made causing a union and we can use UnionFind
        # parent = [1,2,3], rank = [1,1,1]. Rank is size of the graph
        # loop through each edge and connecting them in the shape of the tree
        # so after we loop into [1,2], we will build an edge between 1 and 2 and now rank of 1 is now 2,
        # and we set parent of 2 to 1. parent = [1,1,3], rank = [2,1,1].
        # if rank is lower than it will be the child. parent = [1,1,1], rank = [3,1,1]
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n+1)
        def find(n):
            p = parent[n]
            while p != parent[p] :# keep going until u find the last root parent
                # use path compression to get grandparents in order to ensure shorter path
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: # already merged cannot continue(redundant connection)
                return False
            if rank[p1] > rank[p2]:# means p1 is parent
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2] # since always have connection it will always return true
