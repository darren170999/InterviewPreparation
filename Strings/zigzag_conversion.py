class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Create a grid to add chars to grid
        if numRows == 1:
            return s
        n = len(s)
        grid = [[""] * (n) for _ in range(numRows)]
        i = 0# index into s
        down = True
        r,c = 0, 0
        for i in s:
            if down: # append downwards
                grid[r][c] = i
                r+=1
            else:
                r-=1
                c+=1
                grid[r][c] = i
            if r == numRows:
                r-=1
                down = False
            elif r == 0:
                r+=1
                down = True
        # Loop into grid append to new string
        ans = ""
        for r in range(numRows):
            for c in range(n):
                if grid[r][c] != "":
                    ans += grid[r][c]
        return ans