class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # return list of ints, as many parts as possible
        # every character's start and end are potential partitions
        # use a Hashmap to keep track of where characters end
        # Maintain size of current partition starting from 0
        # and a potential "end" that tells us where the partition might end
        # once u reach end, this means u found your partition, reset and repeat
        hashMap = {}
        n = len(s)
        ans = []
        for i,c in enumerate(s):
            hashMap[c] = i # Cause the later ones will update the keys
        # print(hashMap)
        size, end = 0, 0
        for i in range(n):
            end = max(end, hashMap[s[i]])
            if i == end:
                ans.append(size + 1)
                size = 0
            else:
                size+=1
        return ans