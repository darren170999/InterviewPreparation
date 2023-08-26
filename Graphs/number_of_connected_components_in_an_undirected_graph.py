class Solution: # Union find problems are very similar
    # return number of components in the graph based on these edges, [[0,1], [1,2], [3,4]]
    # connected nodes + contiguous values, individual nodes can be a component
    # RARE QN that uses UNION FIND. This algo helps us find disjoint sets.
    # maintain a parent array with each node inside and index is the nth node.
    # every value in this parent array is the parent of itself. eg. [0,1,2,3,4]
    # maintain another rank array that holds the value of the size of the component
    # this rank array starts from [1,1,1,1,1] for the eg above.
    # Traverse through the edges as given above and update rank and parent 
    # Merging: if they have different parent then we know they havent been merged before
    # maintain ans which we return later. -1 for every union aka update of parent array
    # if parent is the same we just return and dont update anything
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n 
        def find(n1): # find the parent of this node
            res = n1
            while res != par[res]:
                par[res] = par[par[res]] # path compression
                res = par[res]
            return res 
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += raknm[p2]
            return 1
        res = n 
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res    