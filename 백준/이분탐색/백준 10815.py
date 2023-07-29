# import sys
# def read_input():
#     return sys.stdin.readline().rstrip()

# N = int(read_input())
# card_list = sorted(list(map(int,read_input().split())))
# M = int(read_input())
# my_card = (list(map(int,read_input().split())))

# def binary_search(left,right,target):
#     answer = 0
#     while left <= right:
#         mid = (left+right) // 2
#         if target > card_list[mid]:
#             left = mid + 1
#         elif target < card_list[mid]:
#             right = mid - 1
#         elif target == card_list[mid]:
#             answer = 1
#             break
#     return answer

# for i in range(M):
#     print(binary_search(0,N-1,my_card[i]),end= " ")

N = int(input())
card_list = set(map(int,input().split()))
M = int(input())
my_card = list(map(int,input().split()))
for i in range(M):
    print(1 if my_card[i] in card_list else 0,end= ' ')