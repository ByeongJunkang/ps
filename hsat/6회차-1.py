from itertools import combinations

N,K = map(int,input().split())

answer = 10**9
graph = []
for _ in range(N):
    x,y,k = map(int,input().split())
    graph.append([x,y,k])
    


for i in combinations(graph,2):
    print(i)


