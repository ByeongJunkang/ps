from collections import deque
n,w,L = map(int,input().split())
trucks = list(map(int,input().split()))
count = 0
bridge = [0] * w
weight = 0
while True:
    out = bridge.pop(0)
    weight -= out
    count +=1
    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks[0])
            weight += trucks[0]
            trucks.pop(0)
        else:
            bridge.append(0)
    
    if not bridge:
        break

print(count)




