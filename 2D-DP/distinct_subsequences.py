class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        MOD = 10 ** 9 + 7  # Define the modulo value
        ROWS, COLS = len(t), len(s)
        dp = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]
        
        # Base case: If string t is empty, there's one way to match (by removing all characters from s)
        for col in range(COLS+1):
            dp[0][col] = 1
        
        for row in range(1, ROWS+1):
            for col in range(1, COLS+1):
                if s[col-1] == t[row-1]:
                    dp[row][col] = (dp[row-1][col-1] + dp[row][col-1])
                else:
                    dp[row][col] = dp[row][col-1]
        
        return dp[ROWS][COLS] if dp[ROWS][COLS] < MOD else -1
