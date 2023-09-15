# # # 1층 문방구에서 숫자 구매
# # # 준비한 금액은 M우너
# # # 숫자는 0~N-1
# # # 각 숫자 i의 가격은 Pi
# # # 같은 숫자 여러번 가능

# # n = int(input())
# # price = list(map(int,input().split()))
# # m = int(input())
# # result = []
# # tmp =[]
# # def dfs(cnt):
# #     print(tmp)
# #     for i in range(n):
# #         if cnt + price[i] <=m:
# #             tmp.append(i)
# #             result.append(tmp[::])
# #             dfs(cnt+price[i])
# #             tmp.pop()

# # dfs(0)
# # print(result)

# # a = "00001"
# # b = "23"
# # if a > b:
# #     print("a")
# # else:
# #     print("b")


# n = int(input())
# dic = [0 for _ in range(51)]
# price = list(map(int,input().split()))
# for i in range(n):
#     dic[price[i]] = i + 1
# price.sort()
# print(dic)
# print(price)
# m = int(input())