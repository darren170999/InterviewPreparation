class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # return clause
        if len(nums) == 1:
            return [nums.copy()] # or [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for p in perms: # add original numbers removed
                p.append(n)
            ans.extend(perms) # add them to result
            nums.append(n) # clean up here by adding it back
        return ans