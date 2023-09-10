import sys
input = sys.stdin.readline
n = int(input())
result = []
for i in range(n):
    a,b = input().split()
    result.append([int(a),b,i])
result.sort(key= lambda x:(x[0],x[2]))
for tmp in result:
    print(tmp[0], tmp[1])