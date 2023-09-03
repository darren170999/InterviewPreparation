from collections import Counter
def solve(power):
    counter = Counter(power)
    power = sorted(counter.keys())
    n = len(power)
    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = power[0]*counter[power[0]]
    for i in range(1, n):
        dp[i][0] = power[i]*counter[power[i]]+(dp[i-1][1] if power[i] - power[i-1] == 1 else max(dp[i-1])) 
        dp[i][1] = max(dp[i-1])
    return max(map(max, dp))
print(solve([3,3,3,4,4,1,8]))
print(solve([5,2,2,2,2,3,4,5,5,5]))