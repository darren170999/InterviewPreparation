class Solution:
    def countAndSay(self, n: int) -> str:
        def recur(stringInput: str) -> str:
            m = len(stringInput)
            new = ""
            i, j = 0, 0
            while(j < m):
                s = stringInput[i]
                if stringInput[j] == s:
                    j+=1
                else: # Not same
                    count = j-i
                    new += str(count)
                    new += s
                    i = j
            count = j-i
            new += str(count)
            new += s
            i = j
            return new
        if n == 1:
            return "1"
        if n==2:
            return "11"
        tmp = recur("11")
        for i in range(n-3):
            newTmp = recur(tmp)
            # print(newTmp)
            tmp = newTmp
        return tmp