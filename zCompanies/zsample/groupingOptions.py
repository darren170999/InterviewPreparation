@lru_cache(None)
def solution(n, k):
    if n < k:
        return 0
    if n == k:
        return 1
    r = 0
    for i in range(1, min(n - k, k) + 1):
        r += solution(n - k, i)
    return r
    
print(solution(4, 2))
print(solution(7, 3))
print(solution(8, 4))

def generate_options(n, k):
    options = []
    
    def backtrack(current_option, current_sum, remaining_groups):
        if remaining_groups == 0:
            if current_sum == n:
                options.append(current_option.copy())
            return

        for size in range(1, n - current_sum + 1):
            if not current_option or size >= current_option[-1]:
                backtrack(current_option + [size], current_sum + size, remaining_groups - 1)
    
    backtrack([], 0, k)
    return options

# Example usage
people = 8
groups = 4
options = generate_options(people, groups)

for option in options:
    print(option)

