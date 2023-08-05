# import math
# N = int(input())
# num = [i for i in range(10)]
# deungho = ['']+ input().split()
# visited = [0] * 10

# max = 0

# min = math.inf
# result = []
# def dfs(i,k):
    
#     if  i-1== N:
#         result.append(k)
#         return

#     if deungho[i] == "<":
#         for j in range(k%10+1,10):
#             if not visited[j]:
#                 visited[j] = True
#                 dfs(i+1,k*10 + j)
#                 visited[j] = False
        
#     else:
#         for j in range(k%10):
#             if not visited[j]:
#                 visited[j] = True
#                 dfs(i+1,k*10 + j)
#                 visited[j] = False


# for i in range(0,10):
#     visited[i] = True     
#     dfs(1,i)
#     visited[i] = False

# print(result)


import math
N = int(input())
number = [i for i in range(10)]
deungho = input().split()
visited = [0] * 10
result = []
def dfs(num,last_num,temp):

    if num == N:
        result.append(int(temp))
        return
  
    if deungho[num] == '>':  
        for i in range(10):
            if not visited[i]:
                if last_num > i:
                    visited[i] = True
                    dfs(num + 1, i, temp + str(i))
                    visited[i] = False
    else:
        for i in range(10):
            if not visited[i]:
                if last_num < i:
                    visited[i] = True
                    dfs(num + 1, i , temp + str(i))
                    visited[i] = False

for i in range(0,10):
    visited[i] = True
    dfs(0,i,str(i))
    visited[i] = False  

result.sort()
print(result[-1])

if (len(str(result[0]))) == N:
    print(str(0) + str(result[0]))

else:
    print(result[0])

