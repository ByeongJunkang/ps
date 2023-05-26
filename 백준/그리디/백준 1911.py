
import copy
N,M = map(int,input().split())


road = []

for i in range(N):
    a, b = map(int,input().split())
    road.append(a)
    road.append(b)

road.sort()
count = 0
for i in range(len(road)):
    
    if(i+1<len(road)-1):
        break
    dist = 0
    diff = road[i+1] - road[i]
    if diff % M == 1:
        dist = diff // M + 1
    else:
        dist = diff // M 
    
    if road[i] + M *dist >road[i+1]:
        pass

print(count)



