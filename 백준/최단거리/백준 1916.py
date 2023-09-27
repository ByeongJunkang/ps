import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

dis = [10**9] *(n+1)
def disktra(start):

    q= []
    dis[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        length,now = heapq.heappop(q)
        if dis[now] < length:
            continue

        for i in graph[now]:
            cost = length + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

start,end = map(int,input().split())
disktra(start)
print(dis[end])