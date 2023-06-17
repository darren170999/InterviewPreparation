class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        num_dict = set()
        n = len(nums)
        # cannot be the same value but they add up to 0
        for p in range(0, n-2):
            if p > 0 and nums[p] == nums[p-1]:
                continue
            q = p + 1
            r = n - 1
            while q < r:
                total = nums[p] + nums[q] + nums[r]

                if (total == 0):
                    num_dict.add((nums[p],nums[q],nums[r]))
                    q += 1
                    r -= 1
                    while q < r and nums[q] == nums[q-1]:
                        q += 1
                    while q < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    q += 1
            # if r == n - 1 and q == n - 2:
            #     p += 1
            #     q = p + 1
            #     r = q + 1
            # elif r == n - 1:
            #     q += 1
            #     r = q + 1
            # else:
            #     r += 1
        return num_dict