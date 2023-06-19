class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # clue is need recursion for sure
        # When writing a recursion function, must start with terminating clause
        s = []
        ans = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                ans.append("".join(s))
                return
            if openN < n: # still can try add more
                s.append("(")
                backtrack(openN + 1, closedN)
                s.pop()
            if closedN < openN :
                s.append(")")
                backtrack(openN, closedN + 1)
                s.pop()
        
        backtrack(0,0)
        return ans