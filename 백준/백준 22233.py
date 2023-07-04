import sys
N, M = map(int,input().split())
input = sys.stdin.readline
keyword = {}
blog = []
for _ in range(N):
    a = (input().strip())
    keyword[a] = ""

for _ in range(M):
    b = input().strip().split(',')
    for i in range(0,len(b)):
        if b[i] in keyword:
            del keyword[b[i]]
    blog.append(len(keyword))


for i in blog:
    print(i)
            