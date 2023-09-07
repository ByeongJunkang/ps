import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
result = []
a_idx = 0
b_idx = 0
while a_idx < n and b_idx < m:
    if a[a_idx] < b[b_idx]:
        result.append(a[a_idx])
        a_idx +=1
    else:
        result.append(b[b_idx])
        b_idx +=1
while (a_idx < n):
    result.append(a[a_idx])
    a_idx +=1
while (b_idx < m):
    result.append(b[b_idx])
    b_idx +=1
print(*result)