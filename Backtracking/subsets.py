class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subsets = []
        n = len(nums)
        def dfs(index):
            if index >= n:
                ans.append(subset.copy())
                return
            # take 
            subset.append(nums[index])
            dfs(index + 1)
            # dont take
            subset.pop()
            dfs(index + 1)
        dfs(0)
        return ans