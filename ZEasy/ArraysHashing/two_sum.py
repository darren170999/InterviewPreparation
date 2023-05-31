class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myMap = {}
        for i,num in enumerate(nums):
            complement = target - num
            if(complement in myMap):
                return [myMap[complement], i]
            myMap[num] = i
        return []

        #create grid, save indexes, if target met, return current indexes
        # n = len(nums)
        # arr = [[0 for x in range(0,n)] for x in range(0,n)]
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         arr[i][j] = nums[i]+nums[j]
        #         if(arr[i][j] == target):
        #             return [i,j]