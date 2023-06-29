class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # smallest number is always after biggest number 
        # 
        left = 0
        right = len(nums)-1
        while(left<right):
            mid = left + (right-left)//2
            if nums[mid] > nums[right] :
                left = mid+1
            elif nums[mid]< nums[right]:
                right = mid
        # return min(nums)
        return nums[left]