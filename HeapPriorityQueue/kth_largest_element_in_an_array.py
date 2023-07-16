class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for i in nums:
            heapq.heappush(res, -i)
        # print(res)
        for j in range(0,k):
            ans = heapq.heappop(res)

        return -1 * ans