import sys
input = sys.stdin.readline
n = int(input())
drinks = list(map(int,input().split()))
drinks.sort()
tmp = sum(drinks) - drinks[-1]
if tmp %2 == 1:
    print(tmp/2+drinks[-1])
else:
    print(tmp//2+drinks[-1])