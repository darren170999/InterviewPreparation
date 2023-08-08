# Minimum Spanning Tree, Prim's Algorithm, Kruskal Algorithm
class Solution:
    # MST, Prim's algorithm or Kruskal Algo (Textbook problem)
    # 1. Create edges 
    # 2. Prim's Algorithm O(N^2*logN) need heapq to implement
    # Need N-1 edges to create the ans, more than that makes a cycle
    # If lengths are equal maybe it wont affect the final outcome
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # can start anywhere, we run BFS and dont add same node twice
        # Visit (HashSet): We dont add the same node twice, if len == n, we stop
        # Frontier(MinHeap): We add all the node and its corresponding weight in this order (weight, node) and pop the smallest to add to cost and visit. Then the one chosen we will add all the frontiers of that node. Result may have repeated edges in frontier. Hence N^2.
        # Nodes chosen will need to not be in visit to be selected
        # Cost: our answer that we maintain as we traverse through
        n = len(points)
        adj = {i:[] for i in range(n) } # edges in adjacency list
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):# dw to add repeated edges
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[j].append([dist,i])
                adj[i].append([dist,j])# cause its a list at this index
        # print(adj)
        # prim's algo starts here
        visit = set()
        ans = 0
        minHeap = [[0,0]] # starting point
        while len(visit)<n:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue # dont add or remove
            ans += cost
            visit.add(i)
            # next we need to go into every neighbouring node in adj lists
            for neiCost, nei in adj[i]:
                if nei not in visit: # adding neighbouring nodes to frontiers
                    heapq.heappush(minHeap, [neiCost, nei])
        return ans        