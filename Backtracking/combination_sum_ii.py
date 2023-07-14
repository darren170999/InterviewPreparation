class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        if sum(candidates) < target:
            return []
        ans = set()
        candidates.sort()
        subset = []
        minimum = min(candidates)

        def dfs(index, tempSum):
            if tempSum == target:
                temp = subset.copy()
                temp.sort()
                ans.add(tuple(temp))
                return
            if index >= n or tempSum > target or target - tempSum < minimum:
                return
            subset.append(candidates[index])
            dfs(index + 1, tempSum + candidates[index])
            subset.pop()

            # Skip over duplicates
            next_index = index + 1
            while next_index < n and candidates[next_index] == candidates[index]:
                next_index += 1

            dfs(next_index, tempSum)

        dfs(0, 0)
        return [list(combination) for combination in ans]