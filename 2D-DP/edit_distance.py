class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Dp graph is needed m+1 by n+1
        # replace(i+1, j+1), delete(i+1, j), insert(i, j+1)
        # if char is the same no operation is needed.
        n, m = len(word2),len(word1)
        dp = [[0 for x in range(n+1)] for y in range(m+1)]
        for i in range(n+1):
            count = n-i
            dp[m][i] = count
        for j in range(m+1):
            count = m-j
            dp[j][n] = count
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if word1[row] == word2[col]:
                    dp[row][col] = dp[row+1][col+1]
                else:
                    dp[row][col] = 1 + min(dp[row+1][col], dp[row][col+1], dp[row+1][col+1])
        return dp[0][0]