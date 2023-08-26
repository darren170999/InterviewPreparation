class Solution:
    # cannot have a loop and must be all connected. edges:[[0,1],[0,2],[0,3],[1,4]]
    # U are given edges, u need to make some kind of adjlists
    # check if num of visit nodes matches the number of input nodes, graph is connected
    # also if cycle is encountered we instantly return false
    # DFS is used and a visit hashset will track the nodes that we visit
    # use a prev to keep track if its okay to revisit the parent node
    # curr node 1 prev node = 0. Base case of DFS is return true if nothing more to visit
    # default prev value is -1 for the first node we visit which is node 0.
    # Time and Space O(e+v) since we only visit each time once. 
     def validTree(self, n, edges):
        if not n:
            return True
        adj = { i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        def dfs(i, prev):
            if i in visit:# loop found
                return False
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue#skip
                if not dfs(j, i): # if false, loop found
                    return False
            return True
        return dfs(0,-1) and n == len(visit)
