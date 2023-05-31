class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        myset = set()
        while n!=1 and n not in myset:
            myset.add(n)
            new = 0
            while n !=0 :
                r = n%10
                new += r * r # 49
                n = n/10 
            n = new
        return n == 1 # which will evaluate to T or F
