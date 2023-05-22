import math

M = int(input())

arr = list()
for i in range(M):
    a ,b = map(int, input().split())
    nCr = math.comb(b,a)
    arr.append(nCr)


for i in arr:
    print(i)