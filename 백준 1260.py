from collections import deque

N, M, V = map(int,input().split())

Vertex = [[]  for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    Vertex[a].append(b)
    Vertex[b].append(a)
    Vertex[a].sort()
    Vertex[b].sort()



visited = [False] * (N+1) 
def bfs(Graph, V):
    queue = deque()
    queue.append(V)
    visited[V] = True
    while(queue):
        n = queue.popleft()
        print(n, end= ' ')
        for i in Graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            


visited1 = [False] * (N+1) 
    
def dfs(V):
    visited1[V] = True
    print(V,end=' ')
    for i in Vertex[V]:
        if not visited1[i]:
            dfs(i) 
    
    

dfs(V)

print()
bfs(Vertex, V)




