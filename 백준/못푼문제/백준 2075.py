import heapq
N = int(input())

q = []
for _ in range(N):
    a = map(int,input().split())
    for i in a:
        if len(q) < N:
            heapq.heappush(q,i)
        else:
            if q[0] < i:
                heapq.heappop(q)
                heapq.heappush(q,i)

print(q[0])


# 두 번재 풀이

n = int(input())
arr = []

for _ in range(n):
    arr += list(map(int,input().split()))
    arr = sorted(arr,reverse=True)[:n]
print(arr[-1])