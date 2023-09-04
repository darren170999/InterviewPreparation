class Solution:
    def myAtoi(self, s: str) -> int:
        def helper(output: str, flag: str) -> int:
            ans = int(output)
            if flag == "-":
                ans = -1*ans
            if ans < -2**31:
                ans = -2**31
            if ans > 2**31-1:
                ans = 2**31-1
            return ans
        output = "0"
        flag = "+"
        checker = 0
        for i in s:
            if i.isalpha() or i == ".":
                return helper(output, flag)
            if i == " ":
                if checker !=0 or output != "0":
                    return helper(output, flag)
                continue
            if (i == "-" or i=="+"):
                if output != "0":
                    return helper(output, flag)
                checker+=1
                flag = i
                continue
            if checker > 1:
                return helper(output, flag)
            if i.isdigit():
                output += i
        return helper(output, flag)