# 배열에 정수 x 넣기.
# 배열에서 절댓값이 가장 작은 값 출력, 그 값을 배열에서 제거
# 절댓값이 가장 작은 여러개, 가장 작은 수 출력, 그 값을 배열에서 제거

import sys
import heapq
input = sys.stdin.readline
N = int(input())
list = []
answer = []
for _ in range(N):
    num = int(input())
    if num!=0:
        heapq.heappush(list,((abs(num),num)))
    else:
        if list:
            num1,num2 = heapq.heappop(list)
            print(num2)
        else:
            print(0)