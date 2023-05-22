# from collections import deque

# arr = [[0]*8 for _ in range(4)]

# deque.rota


# for i in range(4):
#     arr[i]= list(input())




# def change_minus(arr):
#     tmp = arr[0]    
#     for i in range(7):
#         arr[i] = arr[i+1]
#     arr[i]  = tmp   
#     return arr

# def change_plus(arr):
#     temp = arr[-1]
#     for i in range(len(arr)-1, 0, -1):
#         arr[i] = arr[i-1]
#     arr[0] = temp
#     return arr



# k = int(input())

# def change(arr,m):
    
#     if m == 1:
#         if arr[0][2] == arr[1][6]:
#             pass
#         else:
#             change_minus(arr[1])
#             if arr[1][2] == arr[2][6]:
#                 pass
#             else:
#                 change_plus(arr[2])
#                 if arr[2][2] == arr[3][6]:
#                     pass
#                 else:
#                     change_minus(arr[3])

#     elif m == 2:
#         if arr[0][2] == arr[1][6]:
#             pass
#         else:
#             change_minus(arr[0])

#         if arr[1][2] == arr[2][6]:
#             pass
#         else:
#             change_minus(arr[2])
#             if arr[2][2] == arr[3][6]:
#                 pass
#             else:
#                 change_plus(arr[3])

#     elif m ==3:
#         if arr[2][2] == arr[3][6]:
#             pass
#         else:
#             change_minus(arr[3])

#         if arr[2][6] == arr[1][2]:
#             pass
#         else:
#             change_minus(arr[1])
#             if arr[1][6] == arr[0][2]:
#                 pass
#             else:
#                 change_plus(arr[0])

#     elif m == 4:
#         if arr[3][6] == arr[2][2]:
#             pass
#         else:
#             change_minus(arr[2])
#             if arr[2][6] == arr[1][2]:
#                 pass
#             else:
#                 change_plus(arr[1])
#                 if arr[1][6] == arr[0][2]:
#                     pass
#                 else:
#                     change_minus(arr[0])

    


# def change1(arr,m):
    
#     if m == 1:
#         if arr[0][2] == arr[1][6]:
#             pass
#         else:
#             change_plus(arr[1])
#             if arr[1][2] == arr[2][6]:
#                 pass
#             else:
#                 change_minus(arr[2])
#                 if arr[2][2] == arr[3][6]:
#                     pass
#                 else:
#                     change_plus(arr[3])

#     elif m == 2:
#         if arr[0][2] == arr[1][6]:
#             pass
#         else:
#             change_plus(arr[0])

#         if arr[1][2] == arr[2][6]:
#             pass
#         else:
#             change_plus(arr[2])
#             if arr[2][2] == arr[3][6]:
#                 pass
#             else:
#                 change_minus(arr[3])

#     elif m ==3:
#         if arr[2][2] == arr[3][6]:
#             pass
#         else:
#             change_plus(arr[3])

#         if arr[2][6] == arr[1][2]:
#             pass
#         else:
#             change_plus(arr[1])
#             if arr[1][6] == arr[0][2]:
#                 pass
#             else:
#                 change_minus(arr[0])

#     elif m == 4:
#         if arr[3][6] == arr[2][2]:
#             pass
#         else:
#             change_plus(arr[2])
#             if arr[2][6] == arr[1][2]:
#                 pass
#             else:
#                 change_minus(arr[1])
#                 if arr[1][6] == arr[0][2]:
#                     pass
#                 else:
#                     change_plus(arr[0])
 

        
        
    

          
        

# for i in range(k):
#     m,n = map(int,input().split())
#     if n == 1:
#         change_plus(arr[m-1])
#         change(arr,m)
        
#     else:
#         change_minus(arr[m-1])
#         change1(arr,m)
        

# num = 0
# if arr[0][0] == '1':
#     num = num + 1

# if arr[1][0] == '1':
#     num = num +2

# if arr[2][0] == '1':
#     num = num + 4

# if arr[3][0] == '1':
#     num = num + 8
    

# print(num)