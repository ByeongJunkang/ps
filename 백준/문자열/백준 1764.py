import sys
input = sys.stdin.readline
n,m = map(int,input().split())

set_a = set()
result = []
for _ in range(n):
    tmp = input().rstrip()
    set_a.add(tmp)


for _ in range(m):
    tmp = input().rstrip()
    if tmp in set_a:
        result.append(tmp)

result.sort()
print(len(result))
for i in result:
    print(i)