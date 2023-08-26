from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums
        q = deque()
        ans = []
        for i in range(n):
            limit = i-k+1
            # Remove elements outside the current window from the left
            while q and q[0] < limit: # if leftmost queue should be >= limit
                q.popleft()
            
            # Remove elements smaller than the current element from the right
            while q and nums[q[-1]] < nums[i]: # if curr is < rightmost queue
                q.pop()
            
            # Add the current element to the deque
            q.append(i)
            
            # Add the maximum value for the current window to the output
            if i >= k - 1: # after the original window, we add to output everytime
                ans.append(nums[q[0]])
                
        return ans