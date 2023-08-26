class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #Hint: need PositiveDiag and Negative Diag to keep track
        # its a math thing, to track every cell in the grid
        # posDiag will have r+c and negDiag will have r-c, draw this out to visualise
        # every cell that we enter we will add or remove from the sets below
        # if we place a queen we just check if its violated
        rows = set()
        posDiag = set() # r+c
        negDiag = set() # r-c
        
        grid = [["."] * n for j in range(n)]
        ans = []
        def backtracking(col):
            if col == n: # append the whole col after we reach the end of column
                tmp = ["".join(col) for col in grid]
                ans.append(tmp)
                return
            for r in range(n):
                if r in rows or (r+col) in posDiag or (r-col) in negDiag:
                    # skip ahead
                    continue
                # Update the sets individually
                rows.add(r)
                posDiag.add(r+col)
                negDiag.add(r-col)
                grid[r][col] = "Q" # place the queen here
                backtracking(col+1)
                rows.remove(r)
                posDiag.remove(r+col)
                negDiag.remove(r-col)
                grid[r][col] = "."
        backtracking(0)
        return ans