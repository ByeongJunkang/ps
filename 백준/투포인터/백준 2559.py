# N, K = map(int,input().split())
# num = list(map(int,input().split()))
# new_sum = sum(num[:K])
# result = [new_sum]
# for i in range(N-K):
#     new_sum = new_sum - num[i] + num[i+K]
#     result.append(new_sum)
# print(max(result))
# import math
# N, K = map(int,input().split())
# num = list(map(int,input().split()))

# start =0 
# end = K-1
# max_sum = -1 * math.inf
# sums = sum(num[start:end+1])
# nums = 0
# while end +1 < N:
#     if nums == 0:
#         max_sum = max(sums,max_sum)
#         nums+=1
#     elif nums >=1:
#             sums = sums - num[start]  + num[end+1]
#             max_sum  = max(sums,max_sum)
#             start +=1
#             end+=1
# print(max_sum)

N, K = map(int,input().split())
num = list(map(int,input().split()))
start =0 
end = K-1
max_sum = sum(num[:K])
sums = sum(num[:K])
nums = 0
while end +1 < N:
    sums = sums - num[start]  + num[end+1]
    max_sum  = max(sums,max_sum)
    start +=1
    end+=1
print(max_sum)