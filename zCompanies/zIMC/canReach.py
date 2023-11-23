import math

buff = [[-1 for _ in range(1001)] for _ in range(1001)]


def dfs(c, x1, y1, x2, y2):
    if buff[x1][y1] != -1:
        return buff[x1][y1]

    if math.sqrt(x1 + y1) % 1 == 0:
        return 0
    if (x1 > x2) or (y1 > y2):
        return 0
    if (x1 == x2) and (y1 == y2):
        return 1

    a = dfs(c, x1 + c, y1 + c, x2, y2)
    b = dfs(c, x1 + y1, y1, x2, y2)
    d = dfs(c, x1, y1 + x1, x2, y2)

    if (a == 1) or (b == 1) or (d == 1):
        buff[x1][y1] = 1
    else:
        buff[x1][y1] = 0

    return buff[x1][y1]


def canReach(c, x1, y1, x2, y2):
    if dfs(c, x1, y1, x2, y2) == 1:
        return "Yes"
    return "No"