N, M = map(int,input().split())
num_list = sorted(list(map(int,input().split())))
result = []
real_result = []
visited = [False] * (N+1)
def dfs():
    if len(result) == M:
        real_result.append(result[::])
        return
    for j in range(N):
        if not visited[j]:
            result.append(num_list[j])
            visited[j] = True
            dfs()
            result.pop()
            visited[j] = False
dfs()
data = sorted(list(set(map(tuple,real_result))))
for item in data:
    print(" ".join(map(str, item)))
