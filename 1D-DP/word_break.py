class Solution:
    from collections import deque
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
# Bottom Up approach pls
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n-1, -1, -1):
            for word in wordDict:
                m = len(word)
                # checks for overflow and if word slice are the same
                if i + m <= n and s[i:i+m] == word:
                    dp[i] = dp[i + m]
                if dp[i] is True:
                    break
        # print(dp)
        return dp[0]
        # que = deque(s)
        # ans = []
        # ls = ""
        # while que:
        #     ls += (que.popleft())
        #     if ls in wordDict:
        #         ans.append(ls)
        #         ls = ""
        # if len(ls) != 0:
        #     return False
        # return True
