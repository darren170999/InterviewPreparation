import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k
        heapify(self.nums) # min is left, pop removes min
        # print(self.nums)
        while len(self.nums) > self.k:
            heappop(self.nums)
            # print(self.nums)

        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        elif val > self.nums[0]:
            heapreplace(self.nums, val)
            # print(self.nums)
        return self.nums[0] # need to return min which is the kth
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)