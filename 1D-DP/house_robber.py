class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        temp = 0
        # track robbed values with rob variables
        rob1, rob2 = 0, 0 # only need to maintain the last two maxes
        for i in range(n):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
