class Solution:
    import heapq
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize!=0:
            return False # no way its possible
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0) # use count with key n if key dont exists use 0
        minHeap = list(count.keys())
        heapq.heapify(minHeap) # heapify the keys to be used
        while minHeap:
            first = minHeap[0]
            for i in range(first, first+groupSize):
                if i not in count:
                    return False # key not in count not possible to exists
                count[i] -= 1
                if count[i] == 0:
                    # if i != minHeap[0]:
                    #     return False
                    heapq.heappop(minHeap)
        return True            