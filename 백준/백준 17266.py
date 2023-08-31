# 어두우면 가지 않음
# 굴다리 -> 최단거리, 어두워서 빙빙 돌아감
# 0 ~ N 밝히게 민원
# 가로등 M, 가로등 위치 x
# 높이만큼 주위 비침
# 
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
num_list = list(map(int,input().split()))
max_num = max(num_list[0],N-num_list[-1])

for i in range(1,M):
    tmp = num_list[i] - num_list[i-1]
    if tmp % 2:
        height = tmp//2+1
        
    else:
        height = tmp//2
    max_num = max(height,max_num)
print(max_num)


