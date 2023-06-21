class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            ans = int(str(x)[::-1])
        else:
            ans = int(str(-x)[::-1]) * -1
        left = 2**31 *-1
        right = 2**31 -1
        if ans > right or ans < left:
            return 0
        
        return ans