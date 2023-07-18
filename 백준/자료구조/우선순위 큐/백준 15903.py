
import heapq
n,m = map(int,input().split())
num = list(map(int,input().split()))
heapq.heapify(num)

for _ in range(m):
    a  = heapq.heappop(num)
    b = heapq.heappop(num)
    add = a+b
    heapq.heappush(num,add)
    heapq.heappush(num,add)

print(sum(num))