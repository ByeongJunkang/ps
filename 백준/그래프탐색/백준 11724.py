from collections import deque
N,M = map(int,input().split())
graph =[[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
visited = [False] * (N+1)
for i in range(1,N+1):
    q = deque()
    if not visited[i]:
        visited[i] = True
        ans +=1
        q.append(i)
        while q:
            cur_x = q.popleft()
            for j in graph[cur_x]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = True

print(ans)