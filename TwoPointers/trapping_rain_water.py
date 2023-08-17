class Solution:
    def trap(self, height: List[int]) -> int:
        # water can only be trapped if left and right exists and are higher, water trapped is min(left, right) - itself
        n = len(height)
        ans = 0
        max_left, max_right  = height[0], height[n-1] # look for the next walls
        left, right = 0, n-1 # start and end pointers
        while left< right:
            # update walls every iteration
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)
            # water is trapped between walls, so go from outside inwards to check for trapped water
            # 
            if max_left < max_right:
                ans += max_left- height[left]
                left+=1
            else:
                ans += max_right - height[right]
                right-=1
            # print(max_left, max_right, ans)
        return ans