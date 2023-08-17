class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int: 
        # cannot end early/ prune because the sum can go up and down
        dp = {}
        def dfs(i, total):
            if i == len(nums) and total == target: # end
                return 1
            if i == len(nums) and total!=target:
                return 0
            if (i, total) in dp: # Cache
                return dp[(i, total)]
            dp[(i, total)] = dfs(i+1, total + nums[i])+ dfs(i+1, total - nums[i])
            
            return dp[(i, total)]
        ans = dfs(0, 0)
        return ans