class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # first thing to do is to sort
        intervals.sort(key = lambda i: i[0])
        n = len(intervals)
        ans = [intervals[0]]
        for start, end in intervals[1:]:
            # we need to check whether the curr interval starts before the one in ans ends (Conflict)
            # next we check whether the curr interval ends before or after the the one in ans
            # we keep the one that ends first cause lower chances for it to overlap with the others
            lastEnd = ans[-1][1]
            if start < lastEnd:# conflict
                newEnd = min(end, lastEnd)
                if newEnd == end:
                    ans.pop()
                    ans.append([start,end])
            else:
                ans.append([start, end])
        return n - len(ans) 