# all all the start and end into individual arrays and maintain a count
class Solution:
    def minMeetingRooms(self, intervals):
        start = [i.start for i in intervals]
        start.sort()
        end = [i.end for i in intervals]
        end.sort()
        res, count = 0 ,0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                # s is smaller
                s+=1
                count +=1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res