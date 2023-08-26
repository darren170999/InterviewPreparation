class Solution:
    # Simulataneous BFS from the Gates!
    # Queue is used to track BFS and if its empty means its done
    # when the room is alr filled with soemthing taht is not INF, we will move on
    # O(m+n)
    ROWS, COLS = len(rooms), len(rooms[0])
    visit = set()
    q = deque()
    # Checks for conditions, if true return else add to visited set and new q for further BFS
    def addRoom(r,c):
        if(r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visit or rooms[r][c] == -1):
            return
        visit.add((r,c))
        q.append([r,c])
    # here we add all gates to our BFS queue
    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] = 0:
                q.append([r,c]) 
                visit.add((r,c))
    # init dist to be 0 at the starting point aka gate's position
    dist = 0
    while q:
        # Simultaneous BFS doesnt mean the BFS happen simulataneously
        # it means we one at a time still but it is called level by level 
        # done by usuing queue to track, wtv we append to queue is the order in which we call it
        
        for i in range(len(q)):
            r,c = q.popleft()
            rooms[r][c] = dist
            addRoom(r+1, c)
            addRoom(r-1, c)
            addRoom(r, c+1)
            addRoom(r, c-1)
        dist += 1
