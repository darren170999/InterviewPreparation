def MatrixChallenge(strArr):
    rows = len(strArr)
    if rows == 0:
        return 0

    cols = len(strArr[0])
    matrix = [[0] * cols for _ in range(rows)]
    max_area = 0

    # Initialize the first row of the matrix
    matrix[0] = [int(strArr[0][j]) for j in range(cols)]
    max_area = max(max_area, max(matrix[0]))

    # Build the rest of the matrix and calculate the largest area
    for i in range(1, rows):
        for j in range(cols):
            if strArr[i][j] == '1':
                matrix[i][j] = matrix[i - 1][j] + 1
        max_area = max(max_area, max_histogram_area(matrix[i]))

    return max_area

def max_histogram_area(hist):
    stack = []
    max_area = 0

    for i, h in enumerate(hist):
        while stack and hist[stack[-1]] > h:
            height = hist[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack:
        height = hist[stack.pop()]
        width = len(hist) if not stack else len(hist) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

# Test the function with the given example
strArr = ["10100", "10111", "11111", "10010"]
print(MatrixChallenge(strArr))  # 