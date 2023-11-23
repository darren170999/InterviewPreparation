
from collections import defaultdict, deque
class Solution:
    # Course Schedule I vs Course Schedule II
    # Course Schedule II graph is pre: crs
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        output = []
        while queue:
            curr_course = queue.popleft()
            output.append(curr_course)#
            for crs in graph[curr_course]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    queue.append(crs)#
        if len(output) == numCourses:
            return output
        return []