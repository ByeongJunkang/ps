from collections import deque
N = int(input())
queue = deque()
for i in range(1,N+1):
    queue.append(i)



for i in range(len(queue)-1):
    queue.popleft()
    queue.rotate(-1)

print(queue[0])