import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort() # Sort intervals by start time, normal .sort() will alr do
        queries = sorted(enumerate(queries), key=lambda x: x[1]) # Keep track of query indices and sort based on query
        result = [-1] * len(queries)
        n = len(intervals)
        interval_idx = 0
        active_intervals = [] # Min heap to keep track of intervals
        # We use a min heap to keep track of the active intervals based on their size. 
        # This way, we efficiently maintain the relevant intervals for each query.
        for query_index, query_value in queries:
            # We add intervals to the heap as long as their start times are less than or equal to the current query value. 
            while interval_idx < n and intervals[interval_idx][0] <= query_value: # here alr compared start which is <= query_val
                start, end = intervals[interval_idx]
                # append the interval into the heap with size and end
                size = end - start + 1
                heapq.heappush(active_intervals, (size , end))
                interval_idx += 1
                # print(active_intervals)
            # We also remove intervals from the heap if their end times are less than the current query value. 
            while active_intervals and active_intervals[0][1] < query_value:
                heapq.heappop(active_intervals)
                # print(active_intervals)
            result[query_index] = active_intervals[0][0] if active_intervals else -1

        return result