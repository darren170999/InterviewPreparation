class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates is None:
            return []
        ans = []
        subset = []
        n = len(candidates)
        minimum = min(candidates)
        candidates.sort()
        def dfs(index):
            print(ans)
            if sum(subset) == target and index >= 1: # found
                ans.append(subset.copy())
                return
            if target - sum(subset) < minimum and index >=1: 
                # not possible, dont continue
                return
            if index < 0:
                return 
            subset.append(candidates[index])
            dfs(index) # check after taking
            subset.pop()
            dfs(index -1) # next val

        dfs(n-1)
        return ans