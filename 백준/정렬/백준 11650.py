import sys
input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    a,b = map(int,input().split())
    result.append([a,b])

result.sort(key= lambda x : (x[0],x[1]))
for ans in result:
    print(*ans)