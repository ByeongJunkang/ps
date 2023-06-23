import sys
N,M = map(int,input().split())
time = [int(sys.stdin.readline()) for _ in range(N)]

left = 1
right = answer = max(time) *M

while left <= right:
    mid = (left+right) //2
    num =0
    for i in range(N):
        num += mid // time[i]
    if num >= M:
        right = mid -1
        answer = min(answer,mid)
    else:
        left = mid + 1
print(answer)


