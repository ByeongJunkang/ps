import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    score = []
    for _ in range(N):
        first,second = map(int,input().rstrip().split())
        score.append((first,second))
    
    score.sort(key = lambda x: x[0])
    comp = score[0][1]
    ans = 1
    for i in range(1,N):
        if score[i][1] < comp:
            ans +=1
            comp = score[i][1]

    print(ans)

    

