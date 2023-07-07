# 시간초과
# import sys
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     benefit = 0
#     cost = 0
#     count = 0
#     stock_price = list(map(int,input().rstrip().split()))
#     max_price = max(stock_price)
#     for i,v in enumerate(stock_price):
#         if v < max_price:
#             cost += v
#             count +=1
#         elif v == max_price:
#             benefit += max_price * count - cost
#             if i != N-1:
#                 max_price = max(stock_price[i+1:])
#                 cost = 0
#                 count = 0

#     print(benefit)


# 

import sys
f = sys.stdin.readline


t = int(f())
for i in range(t):
    a = int(f())
    b = list(map(int, f().split()))
    benefit = 0
    b_max = b[-1]
    for j in range(a-2, -1, -1):
        if b[j] > b_max:
            b_max = b[j]
        else:
            benefit += b_max - b[j]

    print(benefit)