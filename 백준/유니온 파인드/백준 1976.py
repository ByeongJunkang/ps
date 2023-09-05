import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
related = [i for i in range(N)]
city = [list(map(int,input().split())) for _ in range(N)]
place = list(map(int,input().split()))
place.sort()
def find(x):
    if related[x] != x:
        related[x] = find(related[x])
    return related[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        related[b] = a
    else:
        related[a] = b


for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            a = find(i)
            b = find(j)
            union(a,b)


for i in range(1,M):
    if find(place[0]-1) != find(place[i]-1):
        print("NO")
        sys.exit()

print("YES") 