import sys
input = sys.stdin.readline
N = int(input())
goal = []
result = []
final = []
for _ in range(N):
    goal.append(int(input())) 

i = 1
idx = 0
while True:
    result.append(i)
    final.append("+")
    while result:
        if idx >= N:
            break
        if result[-1] == goal[idx]:
            final.append("-")
            idx +=1
            result.pop()
        elif result[-1] > goal[idx]:
            print("NO")
            sys.exit()
        else:
            break
    i+=1
    if idx == N:
        break
for i in final:
    print(i)
