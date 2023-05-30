import heapq
import sys
N = int(input())
list = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num!=0:
        heapq.heappush(list,num)
    else:
        if len(list) ==0:
            print(0)
        else:
            print(heapq.heappop(list))

