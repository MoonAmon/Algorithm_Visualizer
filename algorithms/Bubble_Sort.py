from colors import *
import time

def bubble_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size-1):
        for j in range(i+1,size,1):
            if data[j] > data[i]:
                X = data[j]
                data[j] = data[i]
                data[i] = X
                drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))])
                time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])                
