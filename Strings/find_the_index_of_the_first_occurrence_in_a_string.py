class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        n = len(haystack)
        m = len(needle)
        while(i<n):
            if haystack[i:i+m] == needle:
                return i
            i+=1
        return -1