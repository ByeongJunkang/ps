import sys
input = sys.stdin.readline
N = int(input())
tip = [int(input()) for _ in range(N)]
tip.sort(reverse= True)
ans = 0
for i in range(len(tip)):
    if tip[i] - i > 0:
        ans += tip[i] -i
print(ans)