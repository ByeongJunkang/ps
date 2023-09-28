import sys
import heapq
from itertools import combinations
input = sys.stdin.readline
n,e = map(int,input().split())
graph = [[]  for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split())
def dikstra(start):
    dis[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        length,now = heapq.heappop(q)
        if dis[now] < length:
            continue

        for i in graph[now]:
            cost = i[1] + length
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


arr1 = [1,v1,v2,n]
arr2 = [1,v2,v1,n]
tmp = 0
for i in range(3):
    dis = [10**9] * (n+1)
    dikstra(arr1[i])
    tmp += dis[arr1[i+1]]
tmp1 = 0 
for i in range(3):
    dis = [10**9] * (n+1)
    dikstra(arr2[i])
    tmp1 += dis[arr2[i+1]]

ans = min(tmp,tmp1)
if ans >= 10**9:
    print(-1)
else:
    print(ans)
    
# (1,2,3,4), # (1,3,2,4)



