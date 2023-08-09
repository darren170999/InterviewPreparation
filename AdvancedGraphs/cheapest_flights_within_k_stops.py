class Solution:
    # Bellman-ford Algorithm: Another shortest path algorithms.
    # O(Edges*KStops) -> can deal with -ve weights that Djikstra cannot
    # Hard to use Djikstra Algo cause got condition of max k stops -> not efficient
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Need to build Adj list
        # start at src node, do BFS of neighbouring nodes and continue BFS on each of those nodes
        # At the same time, we will keep track of minimum price within k stops as we traverse
        # We will update the temp prices array first before we update the main one
        # the original array represents the previous iteration
        # the temp prices array represents the lowest price we need to pay to reach each node (k)
        # Replace each temp in each iteration before we update the original
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k+1):
            tmpPrices= prices.copy()
            for s,d,p in flights:
                if prices[s] == float("inf"): # not the thing of interest
                    continue
                tmpPrices[d] = min(tmpPrices[d], prices[s] + p)
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]