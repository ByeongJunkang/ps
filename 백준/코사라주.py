import sys
sys.setrecursionlimit(10**6)
V,E = map(int,input().split())

graph = [[]  for _ in range(V+1)]
reversed_graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    reversed_graph[b].append(a)


def dfs(v,visited,stack):
    visited[v] = 1
    for w in graph[v]:
        if visited[w] == 0:
            dfs(w,visited,stack)
    
    stack.append(v)

def reverse_dfs(v,visited,stack):
    visited[v] = 1
    stack.append(v)

    for w in reversed_graph[v]:
        if visited[w] == 0:
            reverse_dfs(w,visited,stack)


            
visited = [0] * (V+1)

stack = []

for i in range(1,V+1):
    if visited[i] == 0:
        dfs(i,visited,stack)

visited = [0] * (V+1)
result = []

while stack:
    ssc = []
    node = stack.pop()
    if visited[node] == 0:
        reverse_dfs(node,visited,ssc)
        print(ssc)
        result.append(sorted(ssc))

print(len(result))
results = sorted(result)
for i in results:
    print(*i,-1)