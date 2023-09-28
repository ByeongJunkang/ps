n,m = map(int,input().split())
num = list(map(int,input().split()))
tmp = sum(num[:m])
ans = tmp
for i in range(m,n):
    tmp = tmp + num[i] - num[i-m]
    ans = max(ans,tmp)
print(ans)
