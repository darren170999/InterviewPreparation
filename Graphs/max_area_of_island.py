class Solution:
    from collections import deque
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        ans = 0
        
        def bfs(row, col, count) -> int:
            q = deque()
            q.append((row,col))
            visited.add((row,col))
            while q:
                count +=1
                row, col = q.popleft()
                direction =[[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in direction:
                    r = dr + row
                    c = dc + col
                    if (r in range(m) and c in range(n) and 
                    (r,c) not in visited and grid[r][c] == 1):
                        q.append((r,c))
                        visited.add((r,c))
            return count
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    count = 0
                    check = bfs(i,j, count)
                    ans = max(check, ans)
        return ans          
                        