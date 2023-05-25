import sys

N = int(input())
money = list()
for i in range(N):
    num = int(input())
    if num !=0:
        money.append(num)
    elif num == 0:
        del money[-1]

sum = 0
for i in money:
    sum = sum + i

print(sum)