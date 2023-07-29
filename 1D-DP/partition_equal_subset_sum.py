class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        if target * 2 != total:
            return False
        dp = set()
        dp.add(0)
        n = len(nums)
        for i in range(n):
            nextDP = set()
            for t in dp:
                nextDP.add(t)
                nextDP.add(t+nums[i])
            dp = nextDP
        if target in dp:
            return True
        return False
# get total sum divide by 2 if its odd no way u can achieve
# nums = [1,5,5,11]
# DP = {0} -> {0,5,11,16,10,21,1,6,12,17,22}
# return True if target in inside