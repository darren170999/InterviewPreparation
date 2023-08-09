# Djikstra Algorithm
class Solution:
    from collections import defaultdict
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Djikstra Algorithm, Find shortest path from the adj list. Rare question O(E*log(V))
        # need BFS and Minheap, Visit to keep track of which ones have been visited
        # MinHeap will keep track of (pathCost, Node)
        # each time we visit a node we will add the frontiers to minHeap
        # to this minHeap and pop the lowest one to visit. 
        # You will update the total that it takes to reach current node plus next node's cost
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v, w)) # doesnt matter if weight comes first
        minHeap = [(0, k)] # starting minheap with the k node
        visit = set() # keep track of what has been visited
        t = 0
        while minHeap:
            # keep poping the smallest thing
            w1, n1 = heapq.heappop(minHeap) # take out the smallest thing
            if n1 in visit:
                continue # skip ahead
            visit.add(n1)
            # t is the cost we want to return, dont need to += because its updated in the BFS
            t = max(t, w1)
            # BFS
            for n2, w2 in adj[n1]: 
                # for unvisited neighbours of current node (n1) in adjacency list
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2 + w1, n2)) # updating the frontiers
        return t if len(visit) == n else -1
