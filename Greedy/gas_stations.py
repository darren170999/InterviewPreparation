class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if solution exists theres only one way to get that
        # unlimited gas total , must know its a greedy problem to solve it with greedy algos
        # return index where you can travel around circuit one time
        if sum(gas) < sum(cost): # guaranteed no solution
            return -1
        total = 0
        res = 0
        n = len(gas)
        for i in range(n): # BECAUSE theres a solution so, since the only condition for this problem is already solved above, we can just loop once and see if you can find starting point, which is wherever the value is positive
            total += gas[i] - cost[i] #
            if total < 0: # only when total dips below 0
                total = 0 # then we need to reset
                res = i + 1 # Will definitely enter here once
        return res