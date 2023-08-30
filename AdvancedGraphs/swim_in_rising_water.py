class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def check(grid, i, j, n, mid, dp):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] > mid or grid[i][j] < 0:
                return 0
            if i == n-1 and j == n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            grid[i][j] = grid[i][j] * -1
            a = (check(grid, i+1, j, n, mid, dp) or
                check(grid, i-1, j, n, mid, dp) or
                check(grid, i, j+1, n, mid, dp) or
                check(grid, i, j-1, n, mid, dp))
            grid[i][j] = grid[i][j] * -1
            dp[i][j] = a
            return dp[i][j]
        n = len(grid)
        mn = 0
        mx = n*n
        ans = 0
        mid = 0
        while mn <= mx:
            dp = [[-1] * n for _ in range(n)]
            mid = ((mx - mn) // 2) + mn
            if check(grid, 0, 0, n, mid, dp):  # If mid is possible, try to minimize it
                ans = mid
                mx = mid - 1
            else:  # If mid is not the answer, update mn to mid + 1
                mn = mid + 1
        return ans