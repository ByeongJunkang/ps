import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().split()))
sum =[0]+[num[0]]+[0] * (n-1)
for i in range(1,n):
    sum[i+1] = sum[i] + num[i]

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    if a == b:
        print(num[a-1])
    else:
        print(sum[b]-sum[a-1])