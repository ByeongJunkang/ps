import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    cnt = 0
    n = int(input())
    origin = list(input())
    goal = list(input())
    W_num = abs(origin.count("W") - goal.count("W"))
    for i in range(n):
        if origin[i] != goal[i]:
            cnt+=1
    if cnt > W_num:
        W_num += int((cnt -W_num)/2)
    print(W_num)
                
