import heapq
import sys
N,M,K = map(int,input().split())

result = []
for _ in range(K):
    a,b = map(int,sys.stdin.readline().split())
    result.append([a,b])

result.sort(key=lambda x: (x[1],x[0]))
find = False

q= []
s = 0
alchol = 0
for i in range(K):
    heapq.heappush(q,result[i][0])
    s += result[i][0]
    alchol = result[i][1]
    if len(q) == N:
        if s >=M:
            find = True
            print(alchol)
            break
        else:
            s -= heapq.heappop(q)

if not find:
    print(-1)  

# n = 기간
# M = 선호도
# k = 맥주 종류
 
# v = 선호도
# c = 레벨


# 하루에 맥주 1병만 가능
# 이전에 받았던 맥주는 수령 불가
# N일 동안 N병이 목표
# 선호도 = 얼마나 좋아하는가
# 도수 레벨 = 얼마나 강한가
# 도수 레벨 > 간 레벨 = 기절
# N개의 선호도 합이 M 이상