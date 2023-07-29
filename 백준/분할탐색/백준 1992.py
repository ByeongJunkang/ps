# import sys
# input = sys.stdin.readline
# N = int(input())
# result = []
# video = []
# for _ in range(N):
#     video.append(list(map(int,input().rstrip())))

# def check(x,y,N):
#     global result
#     if N < 1:
#         return
    
#     isTrue = True
#     first = video[x][y]
#     for i in range(x,x+N):
#         for j in range(y,y+N):
#             if video[i][j] != first:
#                 isTrue = False
#                 break
#         if isTrue == False:
#             break
    
#     if isTrue == True:
#         result.append(first)
#     else:
#         for i in range(2):
#             for j in range(2):
#                 check(x+N//2*i,y+N//2*j,N//2)
# check(0,0,N)
# print(*result)

# import sys
# input = sys.stdin.readline

# N = int(input())
# video = []
# for _ in range(N):
#     video.append(list(map(int, input().rstrip())))

# # 
# def check(x, y, N):
#     # N이 1보다 작으면 return
#     if N < 1:
#         return None
    
#     # 특정 범위 내 숫자들이 
#     isTrue = True
#     first = video[x][y]

#     for i in range(x, x + N):
#         for j in range(y, y + N):
#             if video[i][j] != first:
#                 isTrue = False
#                 break
#         if not isTrue:
#             break
    
#     if isTrue:
#         return str(first)
    
#     else:
#         half_N = N // 2
#         return "(" + check(x, y, half_N) + check(x, y + half_N, half_N) + check(x + half_N, y, half_N) + check(x + half_N, y + half_N, half_N) + ")"

# result = check(0, 0, N)
# print(result)

import sys

def read_input():
    return sys.stdin.readline().rstrip()

def compress_video(x, y, size):
    if size < 1:
        return None
    
    first = video[x][y]
    if all(video[i][j] == first for i in range(x, x + size) for j in range(y, y + size)):
        return str(first)
    else:
        half_size = size // 2
        return f"({compress_video(x, y, half_size)}{compress_video(x, y + half_size, half_size)}" \
               f"{compress_video(x + half_size, y, half_size)}{compress_video(x + half_size, y + half_size, half_size)})"

N = int(read_input())
video = [list(map(int, read_input())) for _ in range(N)]
result = compress_video(0, 0, N)
print(result)
