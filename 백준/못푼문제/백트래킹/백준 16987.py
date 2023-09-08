n = int(input())
eggs = [list(map(int,input().split())) for _ in range(n)]
ans = 0
def dfs(i):
    global ans
    if i == n:
        count = 0
        for i in range(n):
            if eggs[i][0] <= 0:
                count += 1
        if count > ans:
            ans = count
        return
    
    if eggs[i][0] <=0:
        dfs(i+1)
        return
        
    flag = True
    for j in range(n):
        if j == i :
            continue
        if eggs[j][0] > 0:
            flag = False
            break
    if flag:
        ans = max(ans,n-1)
        return

    for j in range(n):
        if i == j or eggs[i][0] <=0:
            continue    
        eggs[j][0] -= eggs[i][1]
        eggs[i][0] -= eggs[j][1]
        dfs(i+1)
        eggs[j][0] +=eggs[i][1]
        eggs[i][0] +=eggs[j][1]
       
dfs(0)
print(ans)

# # def func(eggs,cur):
# #     global max_count
# #     if cur == len(eggs):
# #         count = 0
# #         for i in range(len(eggs)):
# #             if eggs[i][0] <= 0:
# #                 count += 1
# #         if count > max_count:
# #             max_count = count
# #         return

# #     if eggs[cur][0] <= 0:
# #         func(eggs,cur+1)
# #     else:
# #         flag = False
# #         for i in range(len(eggs)):
# #             if i == cur or eggs[i][0] <= 0:
# #                 continue
# #             eggs[cur][0] -= eggs[i][1]
# #             eggs[i][0] -= eggs[cur][1]
# #             flag = True
# #             func(eggs,cur+1)
# #             eggs[cur][0] += eggs[i][1]
# #             eggs[i][0] += eggs[cur][1]
# #         if not flag:
# #             func(eggs, cur+1)
# #     return
# # func(eggs,0)
# # print(max_count)

# eggs = []
# max_count = 0

# def func(eggs,cur):
#     global max_count
#     if cur == len(eggs):
#         count = 0
#         for i in range(len(eggs)):
#             if eggs[i][0] <= 0:
#                 count += 1
#         if count > max_count:
#             max_count = count
#         return

#     if eggs[cur][0] <= 0:
#         func(eggs,cur+1)
#     else:
#         flag = False
#         for i in range(len(eggs)):
#             if i == cur or eggs[i][0] <= 0:
#                 continue
#             eggs[cur][0] -= eggs[i][1]
#             eggs[i][0] -= eggs[cur][1]
#             flag = True
#             func(eggs,cur+1)
#             eggs[cur][0] += eggs[i][1]
#             eggs[i][0] += eggs[cur][1]
#         if not flag:
#             func(eggs, cur+1)
#     return



# def main():
#     global eggs
#     N = int(input())
#     while N:
#         N -= 1
#         tmp = list(map(int,input().split()))
#         eggs.append(tmp)
#     func(eggs,0)
#     print(max_count)
#     return



# if __name__ == "__main__":
#     main()

# n = int(input())
# s = [0]*n
# w = [0]*n

# for i in range(n):
#     s[i], w[i] = map(int, input().split())

# res = 0 
# def solve(idx, eggs):
#     global res
#     if idx == n:
#         cnt = 0
#         for i in range(n):
#             if eggs[i] <= 0:
#                 cnt +=1
#         if cnt > res:
#             res = cnt
#         return

#     if eggs[idx] > 0:
#         for i in range(n):
#             flag = False
#             if eggs[i] > 0 and i != idx:
#                 flag = True
#                 tmp = eggs[:]
#                 tmp[i] -= w[idx]
#                 tmp[idx] -= w[i]
#                 solve(idx+1, tmp)
#         if not flag:
#             solve(idx+1, eggs)
#     else:
#         solve(idx+1, eggs)

# solve(0, s)
# print(res)