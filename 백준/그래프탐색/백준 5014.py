
from collections import deque
F ,S,G,U,D = map(int,input().split())
visited = [False] * 1000001
shortest_path = 0
queue = deque()
queue.append((S,0))
visited[S] = True
def bfs():
    dx = [U,-D]
    global shortest_path
    while queue:
        cur_num,cur_len = queue.popleft()
        if cur_num == G:
            shortest_path = cur_len
            break
        for i in range(2):
            next_x = cur_num + dx[i]
            if next_x >=1 and next_x <= F:
                if not visited[next_x]:
                    queue.append((next_x,cur_len+1))
                    visited[next_x] = True

bfs()
if S != G and shortest_path == 0:
    print("use the stairs")
else:
    print(shortest_path)