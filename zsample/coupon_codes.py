MOD = 1000000007

def modexp(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    if y % 2 == 0:
        t = modexp(x, y // 2)
        return (t % MOD * t % MOD) % MOD
    else:
        t = modexp(x, y // 2)
        return (x % MOD * (t % MOD * t % MOD) % MOD) % MOD

def getVal(arr):
    ans = 0
    for i in range(26):
        if arr[i] > 0:
            ans = (ans % MOD + modexp(i + 1, arr[i]) % MOD) % MOD
    return ans

def compute(s, k):
    arr = [0] * 26
    for i in range(k):
        arr[ord(s[i]) - ord('a')] += 1
    ans = 0
    t = getVal(arr)
    start, end = 0, k - 1
    while end < len(s):
        arr[ord(s[start]) - ord('a')] -= 1
        start += 1
        end += 1
        if end == len(s):
            break
        arr[ord(s[end]) - ord('a')] += 1
        temp = getVal(arr)
        if temp > t:
            t = temp
    return t

# Main code
s = "bcaa"
k = 3
print(compute(s, k))
