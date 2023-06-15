class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if(n==0):
            return 0
        nums.sort()
        ls = [1]
        max_length = 1
        for i in range(0, n-1):
            j = nums[i]
            if (nums[i+1] - j == 1):
                max_length += 1
            elif(nums[i+1] - j < 0 or nums[i+1] - j > 1):
                max_length = 1
            ls.append(max_length)
        return max(ls)
