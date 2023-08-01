import heapq
import sys
input = sys.stdin.readline
V,E = map(int,input().split())

#K = 시작 정점
K = int(input())

road = [[] for _ in range(V+1) ]
# 3~E 간선 (u,v 가중치 w)
for _ in range(E):
    u,v,w = map(int,input().split())
    road[u].append((v,w))

dis = [int(1e9)] * (V+1)
def dik(road,start):
    dis[start] = 0
    q = []
    heapq.heappush(q,[dis[start],start])
    while q:
        dist,cur_start = heapq.heappop(q)
        if dis[cur_start] < dist:
            continue
        for next_node,next_dist in road[cur_start]:
            distance = dist + next_dist
            if distance < dis[next_node]:
                dis[next_node] = distance
                heapq.heappush(q,[distance,next_node])


dik(road,K)
for i in range(1,V+1):
    print("INF" if dis[i] == int(1e9) else dis[i])
