class Solution(object):
    from collections import Counter
    def isAnagram(self, s, t):
        n = len(s)
        if(n == len(t)):
            lsa = Counter(s)
            lsb = Counter(t)
            if(lsa==lsb):
                return True
        return False

        # else:
        #     lsa = []
        #     lsb = []
        #     for i,j in zip(s,t):
        #         lsa.append(i)
        #         lsb.append(j)
        #     lsa.sort()
        #     lsb.sort()
        #     if(lsa == lsb):
        #         return True
        #     else:
        #         return False