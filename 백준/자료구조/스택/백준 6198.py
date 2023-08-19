import sys
input = sys.stdin.readline
N = int(input())
building = []
answer = 0
for _ in range(N):
    building.append(int(input()))
stack = []
for i in range(N):
    while stack:
        if stack[-1] <= building[i]:
            stack.pop()
        else:
            break
    stack.append(building[i])
    answer += len(stack)-1
print(answer)