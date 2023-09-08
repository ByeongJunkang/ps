import sys
input  = sys.stdin.readline
n,k =map(int,input().split())
num = list(map(int,input().split()))
ans = 0
odd = 0
cnt = 0
end = 0
for start in range(n):
    while end < n and odd <= k: 
        if num[end] % 2 == 1:
            odd +=1
        else:
            cnt +=1
        end +=1
        if start ==0 and end == n:
            ans = cnt
            break
    ans = max(cnt,ans)
    if num[start] % 2 == 0:
        cnt -=1
    else:
        odd -=1

print(ans)   


# while end < n and start < n:
#     if num[end] %2== 0:
#         end +=1

#     elif num[end] %2 ==1 and odd < k:
#         odd +=1
#         end +=1

#     elif num[end] % 2 == 1 and odd ==k:
#         start +=1
#         while True:
#             if num[start] % 2 ==0:
#                 break
#             else:
#                 odd -=1
#                 start +=1

#             if start >= end:
#                 break
#     if end !=n:
#         ans = max(ans,end-start-odd+1)
# N, K = map(int, input().split())
# S = list(map(int, input().split()))

# end = 0 # 끝 포인터
# result = 0 # 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이(출력값)
# tmp = 0 # 현재 짝수 부분 수열의 길이
# count = 0 # 지우려는 홀수 카운트

# # start를 N 까지 계속 증가시키며 반복
# for start in range(N):
    
#     # end를 가능한 만큼 이동
#     while (count <= K and end < N):     
        
#         if S[end] % 2 == 1: # 홀수
#             count += 1
#         else: # 짝수
#             tmp += 1
#         end += 1 # 끝 점 이동
        
#         if start == 0 and end == N:
#             result = tmp
#             break
        
#     result = max(tmp, result)
        
#     if S[start] %2 == 1: # 시작점이 홀수
#         count -= 1
#     else: # 시작점이 짝수
#         tmp -= 1
        
# print(result)
