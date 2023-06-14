from collections import deque
T = int(input())
num = 0
answer = []
while num < T:
    M,N,K = map(int,input().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        i,j = map(int,input().split())
        field[j][i] = 1

    visited = [[False] * M for _ in range(N)]
    queue = deque()
    count = 0
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    for a in range(N):
        for b in range(M):
            if not visited[a][b] and field[a][b] == 1:
                count += 1
                queue.append((a,b))
                while queue:
                    cur_x,cur_y = queue.popleft()
                    for i in range(4):
                        next_x = cur_x + dx[i]
                        next_y = cur_y + dy[i]
                        if next_x >=0 and next_x < N and next_y >=0 and next_y <M:
                            if field[next_x][next_y] == 1 and not visited[next_x][next_y]:
                                queue.append((next_x,next_y))
                                visited[next_x][next_y] = True
    
    answer.append(count)
    
    num +=1

for i in answer:
    print(i)