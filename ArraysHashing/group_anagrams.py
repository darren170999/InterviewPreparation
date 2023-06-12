class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs : List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # first init count of letters
            for c in s:
                count[ord(c) - ord('a')] += 1 # increment by 1 to say u found it
            res[tuple(count)].append(s) # use that [0,0,...,0] as key (unique)
        return res.values()