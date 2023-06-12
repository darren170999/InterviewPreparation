import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = defaultdict(int)
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
        top = heapq.nlargest(k,res.values())
        top_keys = [key for key, value in res.items() if value in top]
        return top_keys