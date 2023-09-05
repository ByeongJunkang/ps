import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int,input().split())
parents = [0] * (n+1)
for i in range(1,n+1):
    parents[i] = i

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x]) 
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
for _ in range(m):
    pre,a,b = map(int,input().split())
    if pre == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

