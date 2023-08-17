class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Guaranteed to be within 32-bit if ans exists, unbounded Knapsack
        # need a Dp with amount x coins given
        # if we want to get to this amount with the coin from the same row we look row[i] value to the left
        # if we want to use the remaining coins below curr coin, we look directly below
        # if u cannot get the sum up to amount, means not possible and we add a 0 to it
        n = len(coins)
        Dp = [[0 for i in range(amount+1)] for j in range(n)]
        for j in range(n):
            Dp[j][-1] = 1
        for row in range(n-1, -1, -1):
            for col in range(amount-1, -1, -1):
                if col+coins[row] <= amount:
                    Dp[row][col] += Dp[row][col+coins[row]]
                if row+1 < n:
                    Dp[row][col] += Dp[row+1][col]
                
        return Dp[0][0]