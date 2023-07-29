class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS, queue is normally used for BFS*
        # BFS solution can be easily changed to DFS later**
        # Checks for every 1 in grid, we check to see if there is any adj 1 wrt to it
        # if yes and hasnt been visited before, we call bfs on those new 1s and add the curr to visited
        # recursive call this and when it ends we would have added those numbers to the visited
        # every time the above step happens we will up the count by 1
        if not grid:
            return 0
        count = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def bfs(row, col):
            q = deque()
            visited.add((row,col))
            q.append((row,col))
            while q:
                r,c = q.popleft() # change to dfs by changing this to pop()
                direction = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in direction:
                    newR = r + dr
                    newC = c + dc
                    if (newR in range(m) and newC in range(n) and
                    (newR, newC) not in visited and
                    grid[newR][newC] == "1"):
                        q.append((newR, newC))
                        visited.add((newR,newC))        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs(i,j)
                    count+=1
        return count

