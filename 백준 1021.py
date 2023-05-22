import sys
from collections import deque

N,M = map(int,(sys.stdin.readline().split()))
queue = deque()


line = list(map(int,sys.stdin.readline().split()))

count = 0
for i in range(1,N+1):
    queue.append(i)

for i in range(M):
    cur_v = 1
    for j in range(len(queue)):
        if line[i] == queue[j]:
            break
        else:
            cur_v +=1
    middle = 0
    if len(queue) % 2 == 0:
        middle = len(queue) /2
    else:
        middle = len(queue) //2 + 1
 
    if cur_v > middle:
        num = len(queue)-cur_v +1
        queue.rotate(num)
        queue.popleft()
        count+=num
    else:
        num = cur_v - 1
        queue.rotate(-num)
        queue.popleft()
        count+=num
   
print(count)


