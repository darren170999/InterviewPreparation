def count(length, one_group, zero_group, dp):
    if length < 0:
        return 0
    if length == 0:
        return 1
    if dp[length] != -1:
        return dp[length]
    one = count(length - one_group, one_group, zero_group, dp)
    zero = count(length - zero_group, one_group, zero_group, dp)
    dp[length] = one + zero
    return dp[length]

def main_recursive():
    min_length, max_length, one_group, zero_group = map(int, input().split())
    result = 0
    dp = [-1] * (max_length + 2)
    for length in range(min_length, max_length + 1):
        result += count(length, one_group, zero_group, dp)
    print(result)

def goodBinaryStrings(min_length, max_length, one_group, zero_group):
    dp = [0] * (maxLength + 2)
    dp[0] = 1
    for length in range(1, maxLength + 1):
        if length - one_group >= 0:
            dp[length] += dp[length - one_group]
        if length - zero_group >= 0:
            dp[length] += dp[length - zero_group]
    ans = 0
    for length in range(min_length, max_length + 1):
        ans += dp[length]
    return ans

def main_tabulation():
    min_length, max_length, one_group, zero_group = map(int, input().split())
    result = goodBinaryStrings(min_length, max_length, one_group, zero_group)
    print(result)

# Call the appropriate function
main_tabulation()  # Or main_recursive() for the recursive version
# -------------------------------

class Solution:
    def goodBinaryStrings(
        self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int
    ) -> int:
        mod = 10**9 + 7
        f = [1] + [0] * maxLength
        for i in range(1, len(f)):
            if i - oneGroup >= 0:
                f[i] += f[i - oneGroup]
            if i - zeroGroup >= 0:
                f[i] += f[i - zeroGroup]
            f[i] %= mod
        return sum(f[minLength:]) % mod

// recursive 
#include <bits/stdc++.h>
using namespace std;
int count(int length, int one_group, int zero_group, vector<int> &dp)
{
    if (length < 0)
        return 0;
    if (length == 0)
        return 1;
    if (dp[length] != -1)
        return dp[length];
    int one = count(length - one_group, one_group, zero_group, dp);
    int zero = count(length - zero_group, one_group, zero_group, dp);
    return dp[length] = one + zero;
}