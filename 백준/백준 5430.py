import sys
input = sys.stdin.readline
from collections import deque
T = int(input())

for _ in range(T):
    P = input().rstrip()
    N = int(input())
    symbol = input().rstrip()[1:-1].split(',')
    a = deque(symbol)
        
    if N == 0:
        a = deque()
    flag = 0
    isError = False
    for j in range(len(P)):
        if P[j] == "R":
            flag += 1
        elif P[j] == "D":
            if len(a) == 0:
                print("error")
                break
            else:
                if flag % 2 == 1:
                    a.pop()
                else:
                    a.popleft()  
                
    
    else:
        if flag % 2 == 0:
            print("[" + ",".join(a) + "]")
        else:
            a.reverse()
            print("[" + ",".join(a) + "]")
