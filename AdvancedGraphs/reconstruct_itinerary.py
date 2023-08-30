class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # U will need to run DFS on JFK since we will start from there
        # we need to build a adj list in which we can use it to map out the itinerary
        # First we sort the input lists and when we add the tickets in they will be in order
        # we know its done when len(ans) = len(tickets) + 1
        # To solve deadends, when we meet a deadend, we add it back to the adj[key]
        # Time complexity: Best O(V+E), Worse O(V+E^2), Space complexity: O(E)
        ans = ["JFK"] # start with JFK first
        adj = {i:[] for i,v in tickets}
        tickets.sort()
        for i,v in tickets:
            adj[i].append(v)
        print(adj)
        def dfs(source):
            if len(ans) == len(tickets) +1:
                return True
            if source not in adj: # means one way trip into dest node with no way back
                return False
            temp = list(adj[source])
            for i, v in enumerate(temp):
                adj[source].pop(i) # pop the index of the node u visiting next
                ans.append(v)
                if dfs(v):
                    return True
                adj[source].insert(i,v)
                ans.pop()
                print(adj)
            return False

        dfs("JFK")
        return ans
