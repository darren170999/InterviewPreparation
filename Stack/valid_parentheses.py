class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack. loop into string, find start, if same , pop, else add
        # check is stack is empty at the end -> true
        stack = ['0']
        i = 1
        stack.append(s[0])
        n = len(s)
        while(i<n):
            if(ord(s[i])- ord(stack[-1]) ==2 or ord(s[i])- ord(stack[-1])==1):
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
        if(stack == ['0']):
            return True
        return False