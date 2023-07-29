class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0 and b != 0:
            return b
        if b == 0 and a != 0:
            return a
        return int(log(exp(a) * exp(b))) # math problem