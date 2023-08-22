from collections import deque
N,M = map(int,input().split())
truth_num = list(map(int,input().split()))
truth_set = []
truth_num.pop(0)
group = [[] for _ in range(N+1)]
for j in truth_num:
        for h in truth_num:
            if j!=h:
                group[j].append(h) 
party = []
for _ in range(M):
    temp = list(map(int,input().split()))
    party.append(temp[1:])

for i in party:
    for j in i:
        for h in i:
            if j!=h:
                group[j].append(h) 

visited = [0] * (N+1)
for _ in range(M):
    for num in set(truth_num):
        q = deque()
        visited[num] = True
        for k in group[num]:
            q.append(k)
            truth_num.append(k)
            visited[k] = True
        
        while q:
            cur_x = q.popleft()
            if not visited[cur_x]:
                for k in group[cur_x]:
                    truth_num.append(k)
                    q.append(k)
                    visited[k] = True
                            
    for i in range(N+1):
        if visited[i] == True:
            truth_set.append(i)
ans = 0
for part in party:
    isTrue= True
    for num in part:
        if num in truth_set:
            isTrue = False
            break
    if isTrue:
        ans+=1

print(ans)
