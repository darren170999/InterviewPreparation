class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        subset = []

        def dfs(index):
            if index >= n:
                temp = subset.copy()
                temp.sort()
                if temp not in ans:
                    ans.append(temp)
                return
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            dfs(index + 1)
        dfs(0)
        return ans