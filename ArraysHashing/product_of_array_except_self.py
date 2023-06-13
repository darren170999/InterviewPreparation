class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        if nums.count(0) > 1:
            ans = [0] * n
            return ans
        check = 1
        for i in range(0, n):
            if(nums[i] != 0):
                check = check * nums[i]
        if 0 in nums :
            for i in range(0, n):
                if nums[i] !=0:
                    ans.append(0)
                else:
                    ans.append(check)
        else:
            for i in range(0, n):
                ans.append(check//nums[i])
        return ans