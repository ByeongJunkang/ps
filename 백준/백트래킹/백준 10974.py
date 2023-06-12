N = int(input())

list = [i for i in range(1,N+1)]
num_list = []
# def solution():
#     if len(num_list) == N: 
#             print(*num_list)
#             return
        
#     for i in range(1, N+1):
#     	if i not in num_list:
#             num_list.append(i)
#             solution()
#             num_list.pop()

def solution():
    if len(num_list) == N:
        print(*num_list)
        return

    for i in range(1,N+1):
        if i not in num_list:
            num_list.append(i)
            solution()
            num_list.pop()

solution()
# def generate(arr):
#     stack = []
 
    
#     for i in range(len(list)):
#         used = [False for _ in range(N+1)]
#         stack.append(list[i])
#         while stack:
#             if len(arr) == N:
#                 print(*arr)
#             num = stack.pop(-1)
#             if not used[i]:
#                 arr.append(num)
#                 used[i] = True 
#                 print(arr)
            
        
# generate([])
