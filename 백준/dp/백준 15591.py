import math
import sys
input = sys.stdin.readline
n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, usado = (map(int, input().split()))
    graph[a].append((b, usado))
    graph[b].append((a, usado))


def dfs(k,v):
    visited = [False] * (n+1)
    need_visit = [[v,math.inf]]

    while need_visit:
        cv, usado = need_visit.pop()
        if not visited[cv] and usado >= k:
            visited[cv] = True
            need_visit.extend(graph[cv])
    count = visited.count(True)
    return count - 1

answer = []
for _ in range(q):
    k, v = map(int, sys.stdin.readline().split())
    answer.append(dfs(k, v))

for i in answer:
    print(i)