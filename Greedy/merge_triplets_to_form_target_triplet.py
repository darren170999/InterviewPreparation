class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # indices chosen cannot be a repeat of itself, can do unlimited operations
        # Trick: 1. remove all triplets that have values larger than the target's element
        # using any of those will not allow us to get to target
        # 2. Check if target's element exists in any of the other triplets
        if len(triplets) == 1 and target == triplets[0]:
            return True
        remainding = []
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            else:
                remainding.append(triplet)
        f,s,t = [], [] ,[]
        for i, j, k in remainding:
            f.append(i)
            s.append(j)
            t.append(k)
        if target[0] not in f or target[1] not in s or target[2] not in t:
            return False
        return True