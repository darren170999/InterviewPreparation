class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapify(stones)
        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            z = x - y
            if z < 0:
                heapq.heappush(stones, z)
        if not stones:
            return 0
        return -1 * stones[0]