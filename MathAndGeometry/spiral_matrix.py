class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        ans = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        i, j = 0, 0
        di = 0  # direction index

        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = None  # Mark the visited element as None

            ni, nj = i + directions[di][0], j + directions[di][1]
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] is not None:
                i, j = ni, nj # which i, j in matrix will be appended in next iteration
            else: # Direction Change 
                di = (di + 1) % 4
                i, j = i + directions[di][0], j + directions[di][1]

        return ans