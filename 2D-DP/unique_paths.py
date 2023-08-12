class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # straight forward 2D DP problem
        DP = [[0 for i in range(n+1)] for j in range(m+1)]
        DP[m-1][n-1] = 1
        # print(DP)
        for row in range(m-1,-1,-1):
            for col in range(n-1, -1, -1):
                DP[row][col] = DP[row + 1][col] + DP[row][col+1] + DP[row][col]
        # print(DP)
        return DP[0][0]