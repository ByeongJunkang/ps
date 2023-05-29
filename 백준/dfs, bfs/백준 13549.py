from collections import deque

m,n = map(int,input().split())
road = [0] * 100001
visited = [False] * 100001
queue = deque()
queue.append((m,0))
shortest_path = 0
visited[m] = True
def bfs():
    while queue:
        global shortest_path
        cur_num,cur_len = queue.popleft()
        nx = [-1,1,2* cur_num]
        
        if cur_num == n:
            print("hi")
            shortest_path = cur_len
            break

        for i in range(3):
            if i != 2:
                next_x = cur_num + nx[i]
            else:
                next_x = cur_num * 2
        
            if next_x >=0 and next_x < 100001:
                if not visited[next_x]:
                    if i == 2:
                        queue.append((next_x,cur_len))
                    else:
                        queue.append((next_x,cur_len+1))
                    visited[next_x] = True
                    

bfs()
print(shortest_path)