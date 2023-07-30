class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        check = 0
        flag = False
        def bfs(row,col, newQ, count): # pass in the rotten orange indexes
            q = deque()
            for rr,cc in newQ:
                q.append((rr,cc))
                visited.add((rr,cc))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                temp = []
                while q:
                    temp.append(q.popleft())
                for r,c in temp:
                    for dr, dc in directions:
                        newR = dr + r
                        newC = dc + c
                        if (newR in range(ROWS) and newC in range(COLS) and 
                        (newR,newC) not in visited and grid[newR][newC] == 1):
                            q.append((newR,newC))
                            visited.add((newR,newC))
                            grid[newR][newC] = 2
                count +=1
            return count
        newQ = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2 and (r,c) not in visited:   
                    newQ.append((r,c))
        check += bfs(0,0, newQ, -1)  
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
                if grid[r][c] == 2:
                    flag=True
        if flag:
            return check # only if theres some things to loop
        else:
            return 0