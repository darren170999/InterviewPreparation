class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        vol = 0
        x = n-1
        p = 0
        while p < x:
            temp = min(height[p], height[x]) * (x-p)
            if temp > vol:
                vol = temp
                # diffH = height[x] - height[x-1]
                # diffPH = height[p+1] - height[p]
                # base = (x-p-1)
                # while p < x and height[x] <= (diffH * base):
                #     x -= 1
                # while p < x and height[p] <= (diffPH * base):
                #     p += 1
            if height[p] < height[x]:
                p += 1    
            else:
                x -= 1
        return vol