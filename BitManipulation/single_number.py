class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = defaultdict(int) # add more keys when new things are met
        for num in nums:
            hashmap[num] += 1
        for key, value in hashmap.items():
            if value == 1:
                return key
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         if(len(nums) == 1):
#             return nums[0]
#         for i in nums:
#             if(nums.count(i) == 1): # positive number
#                 return i
            