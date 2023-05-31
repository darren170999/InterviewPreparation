class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r, maxVal = 0, 1, 0
        n = len(prices)
        while(r < n):
            p = prices[r] - prices[l]
            if(p > 0):
                maxVal = max(p , maxVal)
            else:
                l=r
            r+=1
        return maxVal