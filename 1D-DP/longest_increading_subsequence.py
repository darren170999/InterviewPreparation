class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+ dp[j])
        return max(dp)
        # n = len(nums)
        # dp = [1] * (n+1)
        # x = nums[n-1]
        # for i in range(n-1, -1, -1):
        #     if nums[i-1] > nums[i]:
        #         dp[i] = dp[i+1] + 1
        #         x = nums[i]
        #     else:
        #         dp[i] = dp[i+1]
        # print(dp)
        # return dp[0]
