class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: 
                # since sorted order, everything else will not affect, can end earlier
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # wont affect current interval so just add to res
                res.append(intervals[i])
            else:# must merge to find new interval that we will need to insert
                newInterval = [min(intervals[i][0], newInterval[0]) , max(intervals[i][1], newInterval[1])]
        # if res not even appended at all then
        res.append(newInterval)
        return res
