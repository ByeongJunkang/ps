from collections import deque
while True:
    w,h = map(int,input().split())
    if w== 0 and h ==0:
        break

    matrix = []
    for _ in range(h):
        matrix.append(list(map(int,input().split())))
    
    visited = [[False] * w for _ in range(h)]
    result = 0
    def bfs(x,y):
        global result
        dx = [1,0,-1,0,-1,-1,1,1]
        dy = [0,-1,0,1,-1,1,-1,1]
        q = deque()
        q.append((x,y))
        visited[x][y] = True
        while q:
            cur_x, cur_y = q.popleft()
            
            for i in range(8):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if next_x >=0 and next_x < h and next_y >=0 and next_y < w:
                    if matrix[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x,next_y))
                        

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                result+=1

    print(result)
