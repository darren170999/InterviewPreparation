class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        i, j = 0, 0
        m = len(board)
        n = len(board[0])
        path = set() # Track visited
        res = []

        def dfs(r, c, i):# r: row index, c: col index, i: word index
            if i == len(word):
                return True # found
            if (r<0 or c<0 or r>=m or c>=n or word[i] != board[r][c] or (r,c) in path):
                # if out of bounds or if visited before or if curr word not right
                return False

            path.add((r,c)) # learn to use set and tuples to track traversal problems
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))        

            path.remove((r,c))
            return res

        for r in range(m):
            for c in range(n):
                if dfs(r,c,0): return True
        return False