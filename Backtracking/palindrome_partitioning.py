class Solution:
    def partition(self, s:str)-> List[List[str]]:
        res = []
        subset = []
        def isPalindrome(s):
            check = []
            for i in s:
                check.append(s)
            return check == list(reversed(check))
            
        def dfs(index):
            if index >= len(s):
                ans.append(subset.copy())
                return
            # with pruning, dont call DFS all the time
            for i in range(index, len(s)):
                if isPalindrome(s[index: i+1 ]):
                    subset.append(s[index: i+1])
                    dfs(i + 1)
                    subset.pop()# restore / cleanup
        dfs(0)
        return ans
