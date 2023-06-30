class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        for r in range(0, n-m+1): # looping through longer one
            if sorted(s2[r:r+m]) == sorted(s1):
                return True
        return False