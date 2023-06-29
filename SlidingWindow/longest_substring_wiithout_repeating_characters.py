class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, ans = 0, 0
        check = set()
        n = len(s)
        for r in range(n):
            while s[r] in check:
                check.remove(s[l])
                l += 1 
            check.add(s[r])
            ans = max(ans, len(check))
        return ans