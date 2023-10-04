import heapq,sys
input = sys.stdin.readline
n,m = map(int,input().split())
num = list(map(int,input().split()))
q = []
for i in range(n-1):
    heapq.heappush(q,-(num[i+1]-num[i]))

for _ in range(m-1):
    heapq.heappop(q)

print(-sum(q))