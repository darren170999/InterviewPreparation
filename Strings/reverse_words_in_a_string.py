class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split(" ")
        ans = []
        for i in range(len(tmp)-1,-1,-1):
            if tmp[i] != "":
                ans.append(tmp[i])
        return " ".join(ans)