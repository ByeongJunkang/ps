import sys
input = sys.stdin.readline
N = int(input())
table = []
for _ in range(N):
    s,f = map(int,input().split())
    table.append([s,f])

table = sorted(table,key = lambda x:(x[1],x[0]))
last = 0
count = 0
for time in table:
    if time[0] >= last:
        count +=1
        last = time[1]

print(count)
