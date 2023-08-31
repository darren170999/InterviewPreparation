class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #TOPDOWN
        cache = {}
        def dfs(i,j):
            if(i,j) in cache:
                return cache[(i,j)]
            if i>=len(s) and j>= len(p):
                return True
            if j>= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] ==".")
            if (j+1) < len(p) and p[j+1] == "*":
                cache[(i,j)] = (dfs(i, j+2) or (match and dfs(i+1, j)))
                return cache[(i,j)]
            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]
            cache[(i,j)] = False
            return False

        return dfs(0,0)
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         ROWS, COLS = len(p), len(s)
#         dp = [[False for _ in range(COLS+1)] for _ in range(ROWS+1)]
#         dp[ROWS][COLS] = True
#         for r in range(ROWS-1, -1, -1):
#             for c in range(COLS-1, -1, -1):
#                 if s[c] == p[r]:
#                     # dp[r][c] = dp[r][c]
#                 if p[r] == ".":
#                     dp[r][c] = dp[r+1][c+1]
#                 if 


#         return dp[0][0]