N = int(input())

graph = []
order = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[0] * N for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N**2)]

for order in range(N**2):
    result = []
    student = graph[order]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                like, blank = 0,0
                for next in range(4):
                    next_x=  i + dx[next]
                    next_y = j + dy[next]
                    if 0 <= next_x < N and 0 <= next_y < N:
                        if not visited[next_x][next_y]:
                            blank +=1
                        if visited[next_x][next_y] in student[1:]:
                            like +=1
                result.append([like,blank,i,j])
        
    result.sort(key = lambda x:(-x[0],-x[1],x[2],x[3]))
    visited[result[0][2]][result[0][3]] = student[0]

graph.sort()      
real_result = 0

for i in range(N):
    for j in range(N):
        ans = 0
        for k in range(4):
            next_x = i + dx[k]
            next_y = j + dy[k]
            if 0 <= next_x < N and 0 <= next_y < N:
                if visited[next_x][next_y] in graph[visited[i][j]-1]:
                    ans += 1
        if ans != 0:
            real_result += 10 ** (ans-1)
print(real_result)