class Solution:
    def jump(self, nums: List[int]) -> int:
        # guaranteed to reach nums[n-1], want minimum number of jumps
        # idea
        # loop back to front, inner while loop set front to back
        # break if at the first way to reach last
        # update count
        # jump to value
        # repeat until index is 1
        n = len(nums)
        goal = n-1
        count = 0
        while goal > 0:
            left = 0
            flag = True
            while flag and left < goal:
                if left + nums[left] >= goal:
                    flag = False # break while loop
                    count += 1 # best one to choose so increment
                    goal = left
                left += 1
        return count