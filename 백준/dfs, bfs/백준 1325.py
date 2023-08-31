import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
trust = [[] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    trust[b].append(a)

result = []
max_num = 0
for i in range(1,n+1):
    q = deque()
    visited = set()
    q.append(i)
    visited.add(i)
    while q:
        cur_x = q.popleft()
        for next_x in trust[cur_x]:
            if next_x not in visited:
                q.append(next_x)
                visited.add(next_x)

    if len(visited) > max_num:
        result = [i]
        max_num = len(visited)
    elif max_num == len(visited):
        result.append(i)
        max_num = len(visited)
 
print(*result)
    


