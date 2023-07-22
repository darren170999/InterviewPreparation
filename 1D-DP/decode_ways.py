class Solution:
    def numDecodings(self, s: str) -> int:
        #single letter, single digit: 1-9
        n = len(s)
        cache = { n: 1} # cache keeps track of what is visited]
        def dfs(index):
            if index in cache: # if in cache alr dont take
                return cache[index]
            if s[index] == "0": # if 0 dont use
                return 0
            # 1-9
            # case where i take one number
            res = dfs(index + 1)
            # case where I take two numbers
            if index < n-1 and (s[index] == "1" or s[index] == "2" and s[index+1] in "0123456" ):
                res += dfs(index+2)
            cache[index] = res
            return res
        return dfs(0)

