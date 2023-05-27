from collections import deque

N = int(input())
people1, people2 = map(int,input().split())

relation = []
m = int(input())

for i in range(m):
    a = list(map(int,input().split()))
    relation.append(a)


visited= [False for _ in range(m)]

queue = deque()
for i in range(m):
    if people1 in relation[i]:
        queue.append((relation[i],people1,1))
        visited[i] = True

# print(visited)
# print(queue)
shortest_path = 1
cnt = 0
def bfs():
    global shortest_path
    global cnt
    while queue:
        num,cur_num,cur_len= queue.popleft()
        if people2 in num:
            shortest_path = cur_len
            cnt = 1
            break

        if cur_num == num[0]:
            find_num = num[1]
        else:
            find_num = num[0]  
            
        for i in range(m):
            if find_num in relation[i]:
                if not visited[i]:
                    queue.append((relation[i],find_num,cur_len+1))
                    visited[i] = True
       

bfs()
if cnt == 0:
    print(-1)
else:
    print(shortest_path)

