class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        print(dp)
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i< len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j< len(s2) and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0] 
        # # Caching or DP
        # # DP
        # n = len(s1) #col
        # m = len(s2) #row
        # l = len(s3)
        # if n+m != l:
        #     return False
        # dp = [[False for i in range(m+1)] for j in range(n+1)]
        # dp[n][m] = True
        # # for j in range(m-1, -1, -1):
        # #     if s2[j:m] == s3[j+n:l]:
        # #         dp[m][j] = True
        # #     # else:
        # #     #     dp[m][j] = False
        # # for i in range(n-1, -1, -1):
        # #     if s1[i:n] == s3[i+m:l]:
        # #         dp[i][n] = True
        # #     # else:
        # #     #     dp[i][n] = False
        # for row in range(m, -1, -1):
        #     for col in range(n, -1, -1):
        #         # print(s1[row],s2[col], s3[row+col])
        #         if row< m and s1[row] == s3[row+col] and dp[row+1][col]:
        #             dp[row][col] = True
        #         if col<n and s2[col] == s3[row+col] and dp[row][col+1]:
        #             dp[row][col] = True  
        # # print(dp)
        # return dp[0][0]