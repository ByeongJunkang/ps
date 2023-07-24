import sys
input = sys.stdin.readline
n, m = map(int,input().split())
# n = 표의 크기
# m = 구해야하는 합의 개수

matrix = []
for _ in range(n):
    a = list(map(int,input().rstrip().split()))
    matrix.append(a)


for _ in range(m):
    x1,y1,x2,y2 = map(int,input().rstrip().split())
    