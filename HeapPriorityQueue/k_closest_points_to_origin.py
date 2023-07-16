class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # need to use heap to track values
        if len(points) <= k:
            return points
        res = []
        ans = []
        hashMap = {}
        def distance(ls):
            xD = abs(ls[0])
            yD = abs(ls[1])
            return sqrt((xD*xD) + (yD*yD))
        for i in points:
            heapq.heappush(res, (-distance(i), i))
            if len(res) > k:
                heapq.heappop(res) # remove max
            # if hashMap[distance(i)] == None:
            #     hashMap[distance(i)] = i 
            # hashMap[distance(i)]
            # heapq.heappush(res, distance(i))
        ans = [x for (_, x) in res]
        # print(hashMap)
        # print(res)
        # for i in range(k):
        #     index = heapq.heappop(res)
        #     ans.append(hashMap[index])
            # hashMap.pop(index)
        return ans