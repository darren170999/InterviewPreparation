class Solution(object):
    def search(self, nums, target):
        left = 0
        right= len(nums) - 1
        while(left<=right):
            mid = left + (right-left)/2
            if(nums[mid]==target):
                return mid 
            if (nums[mid] >= nums[left]):
                if nums[left] <= target and nums[mid] >= target:
                    right = mid-1
                else:
                    left = mid+1
            elif(nums[mid] <= nums[right]):
                if nums[right] >= target and nums[mid] <= target:
                    left = mid+1
                else:
                    right = mid -1
        return -1