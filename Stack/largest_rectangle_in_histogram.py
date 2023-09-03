class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # treat heights as a stack
        # need to know when to reset width, when to update tmp to new tmp
        ans = 0
        stack = [] # U need a stack to keep track of which (index, height) are worth calculating
        for i, h in enumerate(heights):
            start = i # potentially an index we can consider
            # if stack exists and popped item has a taller height
            while stack and stack[-1][1] > h: # If a lesser height is found and stack exists, we check for new ans 
                index, height = stack.pop()
                ans = max(ans, height * (i - index))
                start = index # means new candidate for start
            stack.append((start, h))
        for i, h in stack: # wtv remaining indexes that are potentially maxAreas
            ans = max(ans, h*(len(heights)- i))
        return ans

        # Hard to create grid and the grid can get huge
        # n = len(heights) # col
        # m = max(heights) # row
        # ans = 0
        # # Create the 2D Grid to represent the Histogram
        # DP = []
        # for i in range(m-1,-1,-1):
        #     column = [1 if i < value else 0 for value in heights] + [0]
        #     DP.append(column)
        # DP.append([0 for i in range(n+1)])
        # for col in range(n-1,-1,-1):
        #     for row in range(m-1, -1, -1):
        #         if row < m-1 and row >= 0 and DP[row][col] != 0:
        #             DP[row][col] = 1 + DP[row+1][col]
        # for col in range(n-1, -1, -1):
        #     for row in range(m-1, -1, -1):
        #         if DP[row][col] != 0:
        #             DP[row][col] += DP[row][col+1]
        #             ans = max(ans, DP[row][col])
        # return ans