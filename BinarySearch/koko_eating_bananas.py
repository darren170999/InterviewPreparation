import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        k_min = math.ceil(sum(piles) / h)
        k_max = max(piles)
        ans = k_max
        l, r = k_min, k_max
        while l < r:
            k = l + (r - l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                r = k
                ans = min(k, ans)
            else:
                l = k + 1

        return int(ans)