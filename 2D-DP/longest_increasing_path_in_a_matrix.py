class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Starting from every path we will need to loop into the neighbouring cells
        # check if its out of bounds
        # if neighbours are larger we add one to the curr grid cell
        # Visited set to check if tis
        m = len(matrix)
        n = len(matrix[0])
        visited = {}

        def dfs(row, col, prev):
            if row < 0 or row == m or col < 0 or col == n or matrix[row][col] <= prev:
                return 0
            if (row, col) in visited:
                return visited[(row, col)]
            ans = 1
            ans = max(ans, 1 + dfs(row + 1, col, matrix[row][col]))
            ans = max(ans, 1 + dfs(row - 1, col, matrix[row][col]))
            ans = max(ans, 1 + dfs(row, col + 1, matrix[row][col]))
            ans = max(ans, 1 + dfs(row, col - 1, matrix[row][col]))
            visited[(row, col)] = ans
            return ans

        result = 0
        for r in range(m):
            for c in range(n):
                result = max(result, dfs(r, c, -1))
        return result