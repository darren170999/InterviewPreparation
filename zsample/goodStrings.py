class Solution:
    M = 1000000007

    def add(x: int, y: int) -> int:
        x += y
        if x >= M:
            x -= M
        return x

    def solution(m1: int, m2: int, g1: int, g0:int) -> int:
        @lru_cache(None)
        def dp(n: int) -> int:
            if n == 0:
                return 1
            if n < 0:
                return 0
            return add(dp(n - g1), dp(n - g0))
        r = 0
        for i in range(m1, m2 + 1):
            r = add(r, dp(i))
        return r

    print(solution(1, 2, 2, 2))

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