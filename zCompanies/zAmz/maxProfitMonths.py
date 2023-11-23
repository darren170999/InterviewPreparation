def solution(v: List[int]) -> int:
    stack = []
    n, r = len(v), 0
    e = [0] * n
    for i in range(0, n):
        while len(stack) and v[stack[-1]] < v[i]:
            # [top..i - 1] is what we want. Note it may contain equal elements.
            r += i - stack.pop()
        if len(stack):
            e[i] = i - stack[-1] if v[stack[-1]] > v[i] else i - stack[-1] + e[stack[-1]] - 1
        else:
            e[i] = i + 1
        r += e[i]
        stack.append(i)
    while len(stack):
        # [top..n - 1] is what we want
        r += n - stack.pop()
    return r - n

print(solution([1, 1, 1, 1]))
print(solution([2, 3, 2]))
print(solution([5, 3, 1, 3, 5]))
print(solution([1, 4, 1, 2, 4, 5, 2, 3, 5,  7, 6, 7, 3, 2, 7, 1, 5, 4, 5, 1, 2, 5, 3, 5]))