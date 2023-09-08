class Solution:
    from collections import Counter
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        tmp = Counter(x for x in magazine)
        check = Counter(y for y in ransomNote)
        tmp.subtract(check)
        for i in tmp:
            if tmp[i] < 0:
                return False
        return True