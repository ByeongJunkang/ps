import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    cnt = 0
    n = int(input())
    origin = list(input())
    goal = list(input())
    w_cnt = 0
    b_cnt = 0
    for i in range(n):
        if origin[i] != goal[i]:
            if origin[i] == "W":
                w_cnt +=1
            else:
                b_cnt +=1

   
    print(max(b_cnt,w_cnt))
                
