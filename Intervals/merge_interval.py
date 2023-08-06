class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda i : i[0]) # must sort first
        ans = [intervals[0]] # supposedly smallest value
        for start, end in intervals[1:]:
            lastEnd = ans[-1][1] # last end in ans
            if start <= lastEnd:
                ans[-1][1] = max(end, lastEnd)
            else:
                ans.append([start,end]) # which will give us new lastEnd
        return ans