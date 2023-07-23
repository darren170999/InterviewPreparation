def findNumberOfWays(n_intervals, n_processes):
    MOD = 10**9 + 7

    # Initialize a 2D DP table to store the number of ways to schedule processes
    # dp[i][j] represents the number of ways to allocate j processes in i intervals
    dp = [[0 for _ in range(n_processes + 1)] for _ in range(n_intervals + 1)]

    # Base case: there is only one way to allocate 0 processes in any number of intervals
    for i in range(n_intervals + 1):
        dp[i][0] = 1

    # Fill the DP table using recurrence relation
    for i in range(1, n_intervals + 1):
        for j in range(1, n_processes + 1):
            # If we schedule a process in the current interval, we must skip the next interval
            dp[i][j] = dp[i - 1][j - 1]
            # If we do not schedule a process in the current interval, we can consider all previous possibilities
            dp[i][j] = (dp[i][j] + dp[i - 1][j] * j) % MOD

    # The result is stored in dp[n_intervals][n_processes]
    return dp[n_intervals][n_processes]

# Example usage:
n_intervals = 3
n_processes = 2
print(findNumberOfWays(n_intervals, n_processes))  # Output: 6