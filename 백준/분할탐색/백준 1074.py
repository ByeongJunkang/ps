# # N ,r,c= map(int,input().split())

# # count = 0
# # def recur(x,y,n):
# #     global count
# #     if x == r and y==c:
# #         print(count)
# #         exit(0)
    
  
    
# #     if not (x<=r<x+n and y<=c < y+n):
# #         count += n*n
# #         return
# #     temp=n//2
# #     recur(x,y,temp)
# #     recur(x,y+temp,temp)
# #     recur(x+temp,y,temp)
# #     recur(x+temp,y+temp,temp)
        

# # recur(0,0,4)
# # print(count)

# import sys


# def visited(n, r, c):
#     global res

#     # 찾는 좌표라면 res를 출력하고 종료
#     if r == R and c == C:
#         print(int(res))
#         exit(0)

#     # 탐색 증인 배열 중에 찾는 좌표가 없다면 좌표에 크기를 더한다.
#     if not (r <= R < r + n and c <= C < c + n):
#         res += n * n
#         return

#     # 1/2/3/4사분면을 재귀적으로 탐색
#     visited(n/2, r, c) # 1사분면
#     visited(n/2, r, c + n/2) # 2사분면
#     visited(n/2, r + n/2, c) # 3사분면
#     visited(n/2, r + n/2, c + n/2) # 4사분면


# N, R, C = map(int, sys.stdin.readline().split())
# res = 0

# # 2^n을 0, 0부터 탐색

# visited(2**N,0,0)




# import sys

# def dc(x,y,n):
#     global cnt
#     if x>r or x+n <= r or y>c or y+n <= c:
#         cnt += n**2
#         return 
    
#     if n > 2:
#         n//=2
#         dc(x,y,n)
#         dc(x,y+n,n)
#         dc(x+n,y,n)
#         dc(x+n,y+n,n)
#     else:
#         if x==r and y==c:
#             print(cnt)
#         elif x==r and y+1==c:
#             print(cnt+1)
#         elif x+1==r and y==c:
#             print(cnt+2)
#         else:
#             print(cnt+3)
#         sys.exit()
        
# n,r,c = map(int,input().split())
# cnt = 0
# dc(0,0,2**n)

import sys
sys.setrecursionlimit(10**9)
n,r,c = map(int,input().split())

res = 0
def search(n,x,y):
    mid = n//2
    global res
    
    if x>r or x+n <= r or y>c or y+n <= c:
        res += n**2
        return 

    if n > 2:
        search(mid,x,y)
        search(mid,x,y+mid)
        search(mid,x+mid,y)
        search(mid,x+mid,y+mid)
    else:
        if x==r and y==c:
            print(res)
        elif x==r and y+1==c:
            print(res+1)
        elif x+1==r and y==c:
            print(res+2)
        else:
            print(res+3)
        sys.exit()

search(2**n,0,0)
print(res)