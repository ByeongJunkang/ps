import heapq
n = int(input())

q = []
for _ in range(n):
    a = list(map(int,input().split()))
    if a[0] == 0:
        if len(q) == 0:
            print(-1)
        else:
            print(-1 * heapq.heappop(q))

    else:
        for i in range(1,a[0]+1):
            heapq.heappush(q,-1 * a[i])

