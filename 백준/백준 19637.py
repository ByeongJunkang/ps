import sys
input = sys.stdin.readline
n,m = map(int,input().split())
standard = {}
for _ in range(n):
    a,b = input().rstrip().split()
    standard[a] = int(b)

print(standard)
for _ in range(m):
    a = int(input())
    print(a)