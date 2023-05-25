from collections import deque

n = int(input())
graph = []
List = []

for i in range(n):
    graph.append(list(map(int, input())))


visited = [[False] *n for _ in range(n)]
count = 0
def bfs(x,y):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    queue = deque()
    num = 0
    queue.append((x,y))
    while(queue):
        cur_x, cur_y = queue.popleft()
        visited[cur_x][cur_y] = True
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if (next_x >=0 and next_y>=0 and next_x<n and next_y <n):
                if(visited[next_x][next_y] == False and graph[next_x][next_y] == 1):
                    queue.append((next_x,next_y))
                    visited[next_x][next_y] = True
                    num += 1
                    # print(next_x,next_y,num)                      
    List.append(num+1)


for i in range(n):
    for j in range (n):
        if(graph[i][j] == 1 and not visited[i][j]):
                bfs(i,j)
                count += 1

print(count)
List.sort()
for i in range(len(List)):
    print(List[i])