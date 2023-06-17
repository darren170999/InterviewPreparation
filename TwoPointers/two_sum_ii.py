class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(numbers): # treat i as pointer
            remainder = target - num
            if remainder in num_dict:
                return [num_dict[remainder] + 1, i + 1]
            num_dict[num] = i
        return None