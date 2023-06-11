import sys

D, N = map(int,input().split())
oven = list(map(int,sys.stdin.readline().split()))
pizza = list(map(int,sys.stdin.readline().split()))
for i in range(len(oven)-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]

dow_loc = 0
left = 0
right = len(oven) - 1
for i in range(N):
    dow = pizza[i]
    is_pilled = False
    cnt = 0
    
    while left <= right:
        middle =(left+right) //2
    
        if oven[middle] >= dow:
            left = middle +1
            dow_loc = middle
            is_pilled = True
             
           
    
        else:
            right = middle -1


    if not is_pilled:
        dow_loc = -1
        break        
    
    left = 0
    right = dow_loc -1


if dow_loc == -1:
    print(0)
else:
    print(dow_loc+1)



   
        
    # j = 0
    # while j<D:
    #     check = 0
    #     if ispizza[j]:
    #         if(j-1)>=0:
    #             if oven[j-1] < pizza[i]:
    #                 print(0)
    #                 cnt +=1
    #                 break
    #             else:
    #                 oven[j-1] = dow
    #         elif j == 0 and i != N-1:
    #             print(0)
    #             cnt +=1
    #             break
            
            
    #     elif not ispizza[j] and dow > oven[j]:
    #         if(j-1) >=0:
    #             oven[j-1] = dow
    #             check +=1
    #             ispizza[j-1] = True
            
    #     if check > 0:
    #         break
    #     j +=1


    # if cnt == 1:
    #     break

    
  






# for k in range(D):
#     if ispizza[k]:
#         print(k+1)
#         break


# import sys

# n, m = map(int,sys.stdin.readline().split())
# oven = list(map(int,sys.stdin.readline().split()))
# pizza = list(map(int,sys.stdin.readline().split()))

# for i in range(1, n) :
#     oven[i] = min(oven[i], oven[i-1])

# idx = 0
# answer = m-1
# for i in range(n-1,-1,-1) :
#     if idx == m :
#         break
#     if oven[i] >= pizza[idx] :
#         idx += 1
#         answer = i

# if idx == m :
#     print(answer + 1)
# else :
#     print(0)