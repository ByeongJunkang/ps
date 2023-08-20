import sys
input = sys.stdin.readline
N = int(input())
num = []
stack = []
answer = []
for _ in range(N):
    num.append(int(input())) 

i = 1
idx = 0
while True:
    stack.append(i)
    answer.append("+")
    while stack:
        if idx >= N:
            break
        if stack[-1] == num[idx]:
            answer.append("-")
            idx +=1
            stack.pop()
        elif stack[-1] > num[idx]:
            print("NO")
            sys.exit()
        else:
            break
    i+=1
    if idx == N:
        break
for ans in answer:
    print(ans)
