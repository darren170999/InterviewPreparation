def sendHiker(queue,queueDir,d,a,search_index,startTime):
ind = queueDir.index(search_index)
arrInd = queue[ind]
out[arrInd] = startTime
queue.pop(ind)
queueDir.pop(ind)
d = 1 if search_index == 1 else 0
a = 1 if search_index == 0 else 0
return queue,queueDir,d,a

out = [-1 for i in range(len(arr))]
a = 0
d = 0
queue = []
startTime = 0
j = 0
while -1 in out:
while j < len(arr) and arr[j] <= startTime:
queue.append(j)
j = j + 1
if len(queue) == 0:
startTime = startTime + 1
continue
queueDir = [dir[i] for i in queue]
for b in queueDir:
if a == 0 and d == 0 and 1 in queueDir:
queue,queueDir,d,a = sendHiker(queue,queueDir,d,a,1,startTime)
elif a == 0 and d == 0 and 0 in queueDir:
queue,queueDir,d,a = sendHiker(queue,queueDir,d,a,0,startTime)
elif d == 1 and 1 in queueDir:
queue,queueDir,d,a = sendHiker(queue,queueDir,d,a,1,startTime)
elif a == 1 and 0 in queueDir:
queue,queueDir,d,a = sendHiker(queue,queueDir,d,a,0,startTime)
else:
queue,queueDir,d,a = sendHiker(queue,queueDir,d,a,b,startTime)
startTime = startTime + 1

Test Scenarios:

arr = [0,0,1,4]
dir = [0,1,1,0]

arr = [0, 1, 1, 3, 3]
dir = [0, 1, 0, 0, 1]

arr = [0, 0, 0, 0]
dir = [0, 0, 1, 1]

arr = [0, 2, 3, 5]
dir = [0, 1, 0, 1]

arr = [1, 2, 3, 4, 5]
dir = [0, 0, 1, 1, 1]

arr = [0, 1, 2, 3, 4]
dir = [0, 1, 0, 1, 0]

arr = [0, 0, 0, 1, 3, 5]
dir = [0, 1, 0, 0, 0, 1]