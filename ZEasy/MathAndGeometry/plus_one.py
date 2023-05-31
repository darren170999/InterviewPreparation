class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        digits[-1] +=1
        digits.insert(0, 0)
        for i in range(n, -1, -1):
            if(digits[i] == 10):
                digits[i] = 0
                digits[i-1] += 1
        if(digits[0] == 0):
            return digits[1:n+1]
        else:
            return digits