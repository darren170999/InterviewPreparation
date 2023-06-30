class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # same sliding window approach
        l = 0
        n = len(s)
        count = {}
        ans = 0
        for r in range(n):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r-l +1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1

            ans = max(ans, r-l+1)
        return ans