import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
start_x,start_y,start_d = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

visited[start_x][start_y] = 1
cnt = 1

while 1:
    flag = 0
    for _ in range(4):
        next_x = start_x + dx[(start_d+3)%4]
        next_y = start_y + dy[(start_d+3)%4]
        start_d = (start_d+3)%4
        if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] == 0:
            if visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1
                cnt += 1
                start_x = next_x
                start_y = next_y
                flag = 1
                break
    if flag == 0: 
        if graph[start_x-dx[start_d]][start_y-dy[start_d]] == 1: 
            print(cnt)
            break
        else:
            start_x,start_y = start_x-dx[start_d],start_y-dy[start_d]