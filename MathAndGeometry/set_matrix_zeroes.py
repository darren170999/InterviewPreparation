class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ls_i = []
        ls_j = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    ls_i.append(i)
                    ls_j.append(j)
        # print(ls_i, ls_j)
        for i in range(n):
            for j in range(m):
                if i in ls_i or j in ls_j:
                    matrix[i][j] = 0