import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    answer = input().rstrip().split()
    if answer[0] == 'add':
        S.add(int(answer[1]))
    elif answer[0] == "check":
        if int(answer[1]) in S:
            print("1")
        else:
            print("0")
    
    elif answer[0] == "remove":
        if int(answer[1]) in S:
            S.discard(int(answer[1]))
    elif answer[0] == "toggle":
        if int(answer[1]) in S:
            S.discard(int(answer[1]))
        else:
            S.add(int(answer[1]))

    elif answer[0] == "all":
        for i in range(1,21):
            S.add(i)
    
    elif answer[0] == "empty":
        S = set()