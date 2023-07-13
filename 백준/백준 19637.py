import sys
input = sys.stdin.readline
n,m = map(int,input().split())
standard = []
for _ in range(n):
    a,b = input().rstrip().split()
    standard.append([a,b])
for _ in range(m):
    a = int(input())
    left = 0
    right = n-1
    while left<=right:
        mid = (left + right) //2
        if int(standard[mid][1]) < a:
            left = mid + 1
        else:
            right = mid- 1
    print(standard[right+1][0])