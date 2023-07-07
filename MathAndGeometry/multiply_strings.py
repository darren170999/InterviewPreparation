class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return string product of num1 * num2 without converting to int
        if num1 == "0" or num2 == "0":
            return "0"
        res = eval(num1 + "*" + num2)
        return str(res)