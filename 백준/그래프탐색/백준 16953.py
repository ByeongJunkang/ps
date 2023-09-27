from collections import deque
import sys
q = deque()
a,b = map(int,input().split())
q.append((a,1))
while q:

    cur_value,cur_time = q.popleft()
    if cur_value == b:
        print(cur_time)
        sys.exit()
    if (cur_value * 10 + 1) <= 10 **9:
        q.append((cur_value*10+1,cur_time+1))
    
    if cur_value * 2 <= 10**9:
        q.append((cur_value*2,cur_time+1))

print(-1)