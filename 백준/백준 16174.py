# 쩰리가 구역 밖으로 나가는 경우 패배
# 쩰리의 출발점은 (0,0)
# 쩨릴의 이동 방향은 오른쪽, 아래
# 쩰리가 가장 오른쪽 아래 칸에 도착하는 경우, 쩰리의 승리
# 한 번에 이동할 수 있는 경우는 현재 밟고 있는 칸에 쓰여 있는 수 만큼
import sys
from collections import deque
dx = [0,1]
dy = [1,0]
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]* n for _ in range(n)]
q = deque()
q.append((0,0,board[0][0]))
visited[0][0] = True
while q:
    cx,cy,cur_time = q.popleft()
    if cx == n-1 and cy == n-1:
        print("HaruHaru")
        sys.exit()
  
    for i in range(2):
        nx = cx + dx[i] * cur_time
        ny = cy + dy[i] * cur_time
        if 0 <=nx < n and 0 <= ny <n:
            if not visited[nx][ny]:
                q.append((nx,ny,board[nx][ny]))
                visited[nx][ny] = True

print("Hing")
