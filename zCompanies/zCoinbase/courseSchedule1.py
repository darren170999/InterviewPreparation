
class Solution:
        # numcourses tells you how many unique courses u have to take
        # use adjacency list data structure which is represented by hashmap
        # crs | pre. if you can clear out the pre to [] then u can complete it
        # 0 | [1,2]
        # 1 | [3,4]
        # 2 | []
        # 3 | [4]
        # 4 | []
        # maps each course to prereq list
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
            