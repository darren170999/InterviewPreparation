class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0] * n
        for i in range(n-2, -1, -1):
            j = i + 1
            while j < n and temperatures[i] >= temperatures[j]:
                if ans[j] > 0:
                    j += ans[j]  # Jump to the next warmer day
                else:
                    break
            if j < n and temperatures[i] < temperatures[j]:
                ans[i] = j - i
        return ans