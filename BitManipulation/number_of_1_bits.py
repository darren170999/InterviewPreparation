class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum((n & (1<<i))!=0 for i in range(32))