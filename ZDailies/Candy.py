# Your solution pass 44/48 TC
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        a = [1] * n
        if n==1:
            return 1
        def check(ans, ratings, n):
            for i in range(n):
                if i == n-1:
                    if ratings[i] > ratings[i-1]:
                        if ans[i] <= ans[i-1]:
                            ans[i] = ans[i-1] + 1
                else:
                    if ratings[i] > ratings[i+1]:
                        if ans[i] <= ans[i+1]:
                            ans[i] = ans[i+1] + 1
                    elif ratings[i] < ratings[i+1]:
                        if ans[i] >= ans[i+1]:
                            ans[i+1] = ans[i] + 1
            return ans
        while True:
            res = sum(a)
            check(a, ratings, n)
            newRes = sum(a)
            if res == newRes :
                return res
# One pass solution with constant space complexity and O(N) tiem
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        
        ret, up, down, peak = 1, 0, 0, 0
        
        for prev, curr in zip(ratings[:-1], ratings[1:]):
            if prev < curr:
                up, down, peak = up + 1, 0, up + 1
                ret += 1 + up
            elif prev == curr:
                up = down = peak = 0
                ret += 1
            else:
                up, down = 0, down + 1
                ret += 1 + down - int(peak >= down)
        
        return ret
# best solution
class Solution:
    def candy(self, ratings):
        number = len(ratings)
        candies = [1] * number

        for i in range(1, number): # looks at curr and prev. Forward dont need to care about candies cause all 1
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(number-2, -1, -1): # from Left to Right POV, looks at curr and next, backwards need to care about candies might be different
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1

        return sum(candies)