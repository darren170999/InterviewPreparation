class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # each element represents how far u can jump, Makes most sense to make a move to the highest one
        # We have a goal that is at the end, we want to loop from the back to the front. If the second last item can reach the goal, the new goal is to get to the second last item. Repeat till the start. If goal == 0, we will return True else False
        n = len(nums)
        goal = n-1
        for i in range(n-1, -1, -1):
            if i+ nums[i]>= goal: # means current index is able to surpass goal
                goal = i
        return True if goal == 0 else False
