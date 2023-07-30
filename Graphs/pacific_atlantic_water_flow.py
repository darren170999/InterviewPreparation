class Solution:
    from collections import deque
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # treat height of ocean to be 0
        # for every cell in heights, which cells can flow to both oceans
        # if condition exists, append to ans
        # maintain two sets, pac, atl which keeps whichever ones can reach the oceans
        ROWS = len(heights)
        COLS = len(heights[0])
        ans = []
        pac, atl = set(), set()
        def dfs(r,c, visit, prevHeight):
            if((r,c) in visit or r<0 or c<0 or r==ROWS or c==COLS or
            heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            # go to all 4 other neighbours, marking all notes that is reachable to either pacific or atlantic oceans
            dfs(r-1,c,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
        for i in range(COLS):
            dfs(0, i, pac, heights[0][i]) # first row Pacific
            dfs(ROWS-1, i, atl, heights[ROWS-1][i]) # last row Atlantic
        for j in range(ROWS):
            dfs(j, 0, pac, heights[j][0]) # first Col pacific
            dfs(j, COLS-1, atl, heights[j][COLS-1])# last col atlantic
        # after the above two for loops, we will have marked every cell that can reach both oceans
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    ans.append([r,c])
        return ans

                
