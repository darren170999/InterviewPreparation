class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            start, end = i, i
            while start>=0 and end< n and s[start] == s[end]:
                start -= 1
                end += 1
                count +=1
            start, end = i, i+1
            while start>=0 and end<n and s[start] == s[end]:
                start -=1
                end += 1
                count+=1
        return count