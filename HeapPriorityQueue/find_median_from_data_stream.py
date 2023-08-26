class MedianFinder:
    # use Heap to track the median's current position. Only the leftmost values in a heap is important.
    # if list is used, add and remove is O(N) but heap(Priority Queue) is O(logN) for both adding and removing
    # leftHeap: MaxHeap and rightHeap: minHeap -> for obvious reasons. Len of both must be +- 1.
    # For every new values, we add to left heap first and if diff in length > 1, we add the leftmost of left heap to right heap
    # leftmost of right heap must be bigger than the leftmost of left heap. Otherwise, repeat above operation to right heap
    # if right heap's length is more than left, we add the leftmost in rightheap to left heap
    def __init__(self):
        self.Oddity = -1 # means even
        self.leftHeap = []
        self.rightHeap = []
    
    def checkDiff(self, left: list, right: list):
        diff = len(left) - len(right)
        return diff # if -ve means right bigger, if +ve means left bigger

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -1 * num)
        if self.checkDiff(self.leftHeap, self.rightHeap) > 1: # means left too big
            value = -1 * heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, value)
        if self.checkDiff(self.leftHeap, self.rightHeap) < -1: # means left too small
            value = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, -1 * value)
        if len(self.leftHeap) >= 1 and len(self.rightHeap) >= 1: # this shouldnt affect lengths
            leftmost = -1 * self.leftHeap[0]
            rightmost = self.rightHeap[0]
            if leftmost > rightmost:
                heapq.heappush(self.rightHeap, leftmost)
                heapq.heappop(self.leftHeap)
                heapq.heappush(self.leftHeap, -1 * rightmost)
                heapq.heappop(self.rightHeap)
        self.Oddity = self.Oddity * -1 # Flip
        # print(self.leftHeap, self.rightHeap, self.Oddity)

    def findMedian(self) -> float:
        if self.Oddity == 1: # means Odd
            if len(self.leftHeap) > len(self.rightHeap):
                # return -1 * heapq.heappop(self.leftHeap)
                return -1 * self.leftHeap[0]
            else:
                # return heapq.heappop(self.rightHeap)
                return self.rightHeap[0]
        else:
            left = -1 * self.leftHeap[0]
            right = self.rightHeap[0]
            return (left + right)/2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()