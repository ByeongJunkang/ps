from collections import deque
N = int(input())
dx = [-1,-2,1,2,-2,-1,2,1]
dy = [2,1,-2,-1,-1,-2,1,2]
answer = []
for _ in range(N):
    queue = deque()
    l = int(input())
    a,b = map(int,input().split())

    target_a, target_b = map(int,input().split())
    chess = [[0] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]
    queue.append((a,b,0))
    while queue:
        cur_x,cur_y,cur_len = queue.popleft()
        if cur_x == target_a and cur_y == target_b:
            print(cur_len)
            break
        for i in range(8):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x >=0 and next_x < l and next_y <l and next_y >=0:
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x,next_y,cur_len+1))
