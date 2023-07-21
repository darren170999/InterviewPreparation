class Solution:
    def rob(self, nums: List[int]) -> int:
        #Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved.
        n = len(nums)
        if n==1:
            return nums[0]
        rob1, rob2 = 0, 0 
        rob3, rob4 = 0, 0
        for i in range(1, n):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        for i in range(0, n-1):
            temp = max(nums[i] + rob3, rob4)
            rob3 = rob4
            rob4 = temp
        return max(rob2, rob4)
