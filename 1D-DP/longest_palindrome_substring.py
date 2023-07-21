class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res=  ""
        n = len(s)
        for i in range(n):
            start, end = i, i
            while start >=0 and end < n and s[start] == s[end]:
                temp = end - start + 1
                if temp > resLen:
                    res = s[start: end+1]
                    resLen = temp
                start -= 1
                end += 1
            start, end = i, i+1
            while start >=0 and end < n and s[start] == s[end]:
                temp = end - start + 1
                if temp > resLen:
                    res = s[start: end+1]
                    resLen = temp
                start -= 1
                end += 1

        return res # any character will do
