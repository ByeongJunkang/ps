import heapq
import sys
input = sys.stdin.readline
N = int(input())
list =[]
ans = 0
for _ in range(N):
    num = int(input())
    heapq.heappush(list,num)

first_length = len(list)
ans = 0
if first_length == 1:
    print(0)
else:
    while True:
        num1 = heapq.heappop(list)
        num2 = heapq.heappop(list)
        ans += num1+num2
        heapq.heappush(list,num1+num2)
        if len(list) == 1:
            break

    print(ans)