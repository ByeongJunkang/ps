N = int(input())
need_list = []
def combination():

    if len(need_list) == N:
        print(*need_list)
        return
    
    for i in range(1,N+1):
        if i not in need_list:
            need_list.append(i)
            combination()
            need_list.pop()

    
    

combination()

# def combination(arr,n):
#     result = []

#     if n == 0:
#         return [[]]
    
#     for i in range(len(arr)):
#         elem = arr[i]
#         for rest in combination(arr[:i]+arr[i+1:],n-1):
#             result.append([elem]+rest)
    
#     return result

# print(combination([1,2,3],2))