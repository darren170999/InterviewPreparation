# from collections import deque
# class Solution:
#     import heapq
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         queue = [] # will keep track of next avail for that task
#         maxHeap = [] # will keep popping most count
#         time = 0
#         for i in set(tasks):
#             heapq.heappush(maxHeap, [-1 * tasks.count(i), i])
#         # task = heapq.heappop(maxHeap)
#         # print(task[0])
#         while (maxHeap and queue) or time == 0:
#             time += 1
#             if maxHeap: # execution of task
#                 task = heapq.heappop(maxHeap)
#                 task[0] += 1 # decrementing count
#                 print(task)
#                 if(task[0] != 0):
#                     task.append(n + time)
#                     queue.append(task)
#                     print(queue)
#                 scheduled = queue.pop(0)
#                 if scheduled[2] <= time:
#                     heapq.heappush(maxHeap, [scheduled[0], scheduled[1]])
#                 else:
#                     queue.append(scheduled)
#             elif maxHeap is None and queue:
#                 scheduled = queue.pop(0)
#                 if scheduled[2] <= time:
#                     heapq.heappush(maxHeap, [scheduled[0], scheduled[1]])
#                 else:
#                     queue.append(scheduled) # idling
#             # if queue:
#             #     scheduled = queue.pop(0)
#             #     if scheduled[2] <= time:
#             #         heapq.heappush(maxHeap, [scheduled[0], scheduled[1]])
#             #     else:
#             #         queue.append(scheduled)
#             print(maxHeap, queue)
#         return time       
from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()  # will keep track of next avail for that task
        maxHeap = []  # will keep popping most count
        time = 0

        for i in set(tasks):
            heapq.heappush(maxHeap, [-1 * tasks.count(i), i])

        while maxHeap or queue:
            # print(maxHeap, queue)
            time += 1

            if maxHeap:
                task = heapq.heappop(maxHeap)
                task[0] += 1  # incrementing count after popping
                if task[0] != 0:
                    task.append(n + time)
                    queue.append(task)

            if queue:
                scheduled = queue.popleft()
                if scheduled[2] <= time and scheduled[0] < 0:
                    heapq.heappush(maxHeap, [scheduled[0], scheduled[1]])
                else:
                    queue.appendleft(scheduled)
            # print(maxHeap, queue)
            # print()

        return time
        