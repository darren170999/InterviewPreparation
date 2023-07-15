class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        subset=[]
        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def dfs(index, ls):
            if len(ls) == len(digits):
                res.append(ls)
                return
            for c in digitsToChar[digits[index]]:
                dfs(index+1, ls+c)
        if digits:
            dfs(0, "")
        return res