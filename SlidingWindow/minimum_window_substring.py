class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding Window, O(m+n)
        # if s size is smaller than t, no way that is possible return ""
        # init hashmap of t for constant lookup time and a hashmap of substring of s.
        # init pointer start and end to be 0,0, increase end until hashmap of ss == hashmap of t
        # start increasing "start" pointer and if chars are met by it, decrease that char and increase end pointer
        # end pointer will increase count while start pointer will decrease count
        s_size, t_size = len(s), len(t)
        if s_size < t_size:
            return ""
        start, end = 0, 0
        hashMap = {}
        for i, c in enumerate(t):
            if c in hashMap:
                hashMap[c] += 1
            else:
                hashMap[c] = 1
        ssHashMap = {}
        for i, c in enumerate(t):
            ssHashMap[c] = 0
        min_length = 100001 # set to upper bound of m,n
        ans = ""
        while end < s_size:
            if s[end] in ssHashMap:
                ssHashMap[s[end]] += 1
            # 'all' function takes in params and check if they all output true
            # check if curr window has all the chars needed: true means potential window is found
            while all(ssHashMap[char] >= hashMap[char] for char in hashMap): 
                if end - start + 1 < min_length: # update potential window and length
                    min_length = end - start + 1
                    ans = s[start: end + 1]
                if s[start] in ssHashMap:
                    ssHashMap[s[start]] -= 1
                start += 1
            end += 1
        return ans

