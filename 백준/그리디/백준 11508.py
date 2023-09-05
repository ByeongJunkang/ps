import sys
input = sys.stdin.readline
N = int(input())
goods = [int(input()) for _ in range(N)]
goods.sort(reverse=True)

for i in range(len(goods)):
    if (i+1) % 3 == 0:
        goods[i] = 0
print(sum(goods))