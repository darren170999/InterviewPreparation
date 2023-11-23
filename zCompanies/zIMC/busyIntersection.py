from collections import deque

def getResult(arrival, street): 
    
    time = 0 # time is the current time in seconds
    idx = 0 # idx is the index of the car that is currently passing through the intersection
    last = 1  # variable that can be either 0 or 1. 0 means that the last car to pass through the intersection was on the main street. 1 means that the last car to pass through the intersection was on the first street. 
    q1, q0 = deque(), deque() 
    ans = [0] * len(arrival) # ans is the array of integers where ans[i] is the time in seconds that the ith car passes through the intersection
    
    while True: 
        move = True # we use this variable to check if we need to increase time or not. If we don't increase time, then we need to check if there are any cars that arrive at the same time as the current time

        # add cars to queue, same logic below
        while idx < len(arrival) and arrival[idx] == time: 
            if street[idx] == 0: # if the car is on the main street
                q0.append(idx)
            else: # if the car is on the first street
                q1.append(idx)
            idx += 1 # increment idx since we have added the car to the queue
    
        if q0 and not q1: # if there are cars on the main street but no cars on the first street
            last = 0 # set last to 0 since the last car to pass through the intersection was on the main street

        while last == 1 and q1: # if there are cars on the first street but no cars on the main street
            ans[q1.popleft()] = time # pop the first car on the first street and set its time to the current time
            time += 1 # increase time by 1 second
            move = False # set move to False since we have moved a car
            while idx < len(arrival) and arrival[idx] == time: # if there are cars that arrive at the same time as the current time
                if street[idx] == 0: # if the car is on the main street
                    q0.append(idx)
                else: 
                    q1.append(idx)
                idx += 1 # increment idx since we have added the car to the queue

        while last == 0 and q0: # if there are cars on the main street but no cars on the first street
            ans[q0.popleft()] = time # pop the first car on the main street and set its time to the current time
            time += 1 # increase time by 1 second
            move = False # set move to False since we have moved a car
            while idx < len(arrival) and arrival[idx] == time: # if there are cars that arrive at the same time as the current time
                if street[idx] == 0:
                    q0.append(idx)
                else:
                    q1.append(idx)
                idx += 1 # increment idx since we have added the car to the queue

        if not q0: # if there are no cars on the main street
            last = 1 # set last to 1 since the last car to pass through the intersection was on the first street
        # need to move on time
        # not += 1 because fail corner case [0, 100000]
        if move: # if we need to increase time
            time = arrival[idx] # set time to the arrival time of the next car that arrives
            continue # continue since we don't need to check if there are any cars that arrive at the same time as the current time
        # finish all cars
        if not q0 and not q1 and idx == len(arrival): # if there are no cars on the main street, no cars on the first street, and we have reached the end of the arrival array
            return ans # return ans since we have finished all cars