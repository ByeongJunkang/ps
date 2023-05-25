import sys
from collections import deque
input = sys.stdin.readline().rstrip()

N = int(input)
queue = deque()

for _ in range(N):
    order = sys.stdin.readline().rstrip().split()
    if "push_back" in order:
        queue.append(int(order[1]))
    elif "push_front" in order:
        queue.appendleft(int(order[1]))
    elif "pop_front" in order:
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif "pop_back" in order:
        if len(queue) > 0:
            print(queue.pop())
        else:
            print(-1)
    elif "size" in order:
        print(len(queue))

    elif "empty" in order:
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif "front" in order:
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif "back" in order:
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)        
        

