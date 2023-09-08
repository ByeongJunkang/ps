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
