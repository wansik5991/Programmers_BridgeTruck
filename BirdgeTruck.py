import os
from collections import deque

def solution(bridge_length, weight, truck_weights):

    truck_waiting = deque([bridge_length, w] for w in truck_weights)
    on_road = deque([truck_waiting[0]])
    truck_waiting.popleft()
    time = 1
    while not(len(on_road) == 0 and len(truck_waiting) == 0) :
        time += 1
        on_road = deque(list(map(lambda x : [x[0] - 1, x[1]], on_road)))
        if on_road[0][0] == 0 :
            on_road.popleft()
        if len(truck_waiting) != 0 and sum(map(lambda x: x[1], on_road)) + truck_waiting[0][1] <= weight :
            on_road.append(truck_waiting[0])
            truck_waiting.popleft()

    return time

os.system('cls')
print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
