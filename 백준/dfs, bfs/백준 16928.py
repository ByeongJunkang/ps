from collections import deque
N,M = map(int,input().split())
game = [0] * 101
visited = [True] + [False] * 100
dx = [1,2,3,4,5,6]
for _ in range(N+M):
    a,b = map(int,input().split())
    game[a] = b
queue = deque()
queue.append((1,0))
shortest_length = 0
is100 = False
def bfs():
    while queue:
        cur_num,cur_len = queue.popleft()
        global shortest_length
        if cur_num == 100:
            shortest_length = cur_len
            break
        for i in range(6):
            next_x = cur_num + dx[i]
            if next_x > 100:
                continue
            else:
                if not visited[next_x] and game[next_x] != 0:
                    visited[game[next_x]] = True
                    queue.append((game[next_x],cur_len+1))
                elif not visited[next_x] and game[next_x] == 0:
                    visited[next_x] = True
                    queue.append((next_x,cur_len+1))

bfs()
print(shortest_length)