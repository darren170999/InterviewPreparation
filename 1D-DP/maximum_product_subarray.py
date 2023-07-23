class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            tmp = n * curMax
            curMax = max(n, n*curMax, n*curMin)
            curMin = min(n, tmp, n*curMin)
            ans = max(ans, curMax)
        return ans
        # n = len(nums)
        # ans = min(nums)
        # def mul(ls: List[int]):
        #     total = 1
        #     for i in ls:
        #         total = total * i
        #     return total
        # for x in range(n): #0,1,2,3
        #     for i in range(x+1):
        #         ans = max(ans, mul(nums[i:n-x+i]))
        # return ans
            