class Solution:
    # Pure Recursion: O(2^n), DP(Cache): O(n)
    def maxProfit(self, prices: List[int]) -> int:
        # Caching question, we cache the index and buy/sell boolean. We need to keep track of this
        # After every sell is a cooldown, cooldowns are just skips, index += 2 else index += 1
        # Caching usually used with hashmaps
        dp = {} # key=(i,buying), val = max_profits
        def dfs(i, buying):
            # Base cases:
            if i >= len(prices):
                return 0
            if (i, buying) in dp: # alr been cached, so return the best possible
                return dp[(i, buying)]
            # Buying + Cooldown
            if buying:
                buy = dfs(i+1, not buying) - prices[i] # the previous best possible case + curr price
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            # Selling + Cooldown
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)