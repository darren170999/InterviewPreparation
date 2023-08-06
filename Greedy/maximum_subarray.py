class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        currSum = 0
        for i in nums:
            if currSum <0:
                currSum = 0 # reset
            currSum += i
            ans = max(ans, currSum)
        return ans