class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        DP = [[0 for j in range(m+1)] for i in range(n+1)]
        for row in range(n-1,-1,-1):
            for col in range(m-1,-1,-1):
                if text1[row] == text2[col]:
                    # take diagonal instead of max of left and down
                    DP[row][col] = DP[row+1][col+1] + 1 
                    # DP[row][col] = max(DP[row+1][col], DP[row][col+1]) + 1
                else:
                    DP[row][col] = max(DP[row+1][col], DP[row][col+1])
        return DP[0][0]
