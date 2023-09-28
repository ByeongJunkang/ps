import sys
import math
input = sys.stdin.readline
n = int(input())
min_num = [0,0,0]
max_num = [0,0,0]
for _ in range(n):
    a,b,c = map(int,input().split())
    min_num = [a+min(min_num[:2]),b+min(min_num),c+min(min_num[1:])]
    max_num = [a+max(max_num[:2]),b+max(max_num),c+max(max_num[1:])]

print(max(max_num),min(min_num))