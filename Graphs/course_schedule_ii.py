class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # TOPO Sort, need to build adjacency lists with DFS,
        # once added to output u dont need to add another course again
        # cross out those nodes from prereq and check the other nodes in the DFS path
        # 
        preMap = {i: [] for i in range(numCourses)} # this is a adj list
        output = []
        visitSet = set()
        cycleSet = set()
        for crs, pre in prerequisites: # adding items to list
            preMap[crs].append(pre)
        # NOTE: A course has 3 possible states
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle
        def dfs(crs):
            if crs in cycleSet: # cycle detected
                return False
            if crs in visitSet: # alr visited
                return True
            cycleSet.add(crs) # so if we meet this again we know a cycle exists
            for pre in preMap[crs]:
                if dfs(pre) == False: #means cycle found
                    return False
            cycleSet.remove(crs) # must rmb to remove cause we going back
            visitSet.add(crs)
            output.append(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs): return []
        return output