# import sys
# N= int(input())
# card = list(map(int,sys.stdin.readline().rstrip().split()))
# M = int(input())
# num = list(map(int,sys.stdin.readline().rstrip().split()))
# card.sort()
# answer = [0] * M
# def binary_search(target,left,right,num):
#     while left <= right:
#         middle = (left + right) //2
#         if card[middle] == target:
#             answer[num] += 1
#             i = 1
#             while True:
#                 if middle - i >=0:
#                     if card[middle-i] == target:
#                         answer[num] += 1
#                         i+=1
#                     else:
#                         break
#                 else:
#                     break
                
#             j = 1
#             while True:
#                 if middle + j < N:
#                     if card[middle +j] == target:
#                         answer[num] +=1
#                         j+=1 
#                     else:
#                         break
#                 else:
#                     break        
#             break
#         elif target > card[middle]:
#             left = middle + 1
#         elif target < card[middle]:
#             right = middle -1
# for i in range(M):
#     binary_search(num[i],0,N-1,i)
# print(*answer)

# import sys

# N = int(input())
# card = list(map(int, sys.stdin.readline().rstrip().split()))
# M = int(input())
# num = list(map(int, sys.stdin.readline().rstrip().split()))
# card.sort()
# answer = [0 for _ in range(M)]

# def binary_search(target, left, right, num):
#     found = False
#     while left <= right and not found:
#         middle = (left + right) // 2
#         if card[middle] == target:
#             answer[num] += 1
#             found = True
#             i = 1
#             while middle - i >= 0 and card[middle - i] == target:
#                 answer[num] += 1
#                 i += 1
#             j = 1
#             while middle + j < N and card[middle + j] == target:
#                 answer[num] += 1
#                 j += 1
#         elif target > card[middle]:
#             left = middle + 1
#         elif target < card[middle]:
#             right = middle - 1

# for i in range(M):
#     binary_search(num[i], 0, N - 1, i)

# print(*answer)
from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))