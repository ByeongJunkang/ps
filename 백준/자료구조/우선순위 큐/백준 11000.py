# (3)
# (1,3)
# (2,4)
# (3,5)
import heapq
import sys
input = sys.stdin.readline
list = []
temp = []
N = int(input())
for _ in range(N):
    s,f = map(int,input().split())
    temp.append((s,f))
temp.sort()
for i in temp:
    s,f = i[0],i[1]
    if list:
        b,a = heapq.heappop(list)
        if b <= s:
            heapq.heappush(list,(f,s))
        else:
            heapq.heappush(list,(b,a))
            heapq.heappush(list,(f,s))
    else:
        heapq.heappush(list,(f,s))

print(len(list))