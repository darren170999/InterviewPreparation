class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a , b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == "/":
                a , b = stack.pop(), stack.pop()
                stack.append(int((b + 0.5)/ a))
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(i))
        return stack[0]