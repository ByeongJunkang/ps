import sys
input = sys.stdin.readline
n = int(input())
tmp = [int(input()) for _ in range(n)]
tmp.sort()
ans = 0
for i in range(len(tmp)):
    ans = max(ans,(tmp[i] * (n-i)))
print(ans)
