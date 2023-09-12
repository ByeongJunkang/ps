import sys
input = sys.stdin.readline
n,k = map(int,input().split())
loc = list(map(int,input().split()))
new_loc = [0] * (n+1)
for i in range(1,n+1):
    new_loc[i] = loc[i-1] + new_loc[i-1]
if k < new_loc[-1]:
    for i in range(n):
        if new_loc[i] <=k < new_loc[i+1]:
            print(i+1)
            break
elif k == new_loc[-1]:
    print(n)
else:
    new_k = new_loc[-1] - (k-new_loc[-1])
    for i in range(n,0,-1):
        if new_loc[i-1] <new_k <= new_loc[i]:
            print(i)
            break
