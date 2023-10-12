n,l = map(int,input().split())
road = [list(map(int,input().split())) for _ in range(n)]
ans = 0

def check(road):
    visited = [False] * n
    for i in range(1,n):
        if abs(road[i] - road[i-1]) >=2:
            return False
        if road[i] < road[i-1]:
            for idx in range(l):
                if idx + i >= n or road[i] != road[i+idx] or visited[idx+i]:
                    return False
                visited[i + idx] = True
           
        elif road[i] > road[i-1]:
            for idx in range(l):
                if i - idx - 1 <0 or road[i-1] != road[i-idx-1] or visited[i-idx-1]:
                    return False
                visited[i-idx-1] = True
                
    return True


for i in range(n):
    if check([road[i][j] for j in range(n)]):
        ans += 1

for j in range(n):
    slope = [False] * n
    if check([road[i][j] for i in range(n)]):
        ans += 1

print(ans)