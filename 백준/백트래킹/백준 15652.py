M,N = map(int,input().split())

answer = list()
def dfs(start):

    if len(answer) == N:
        print(*answer)
        return
    
    for i in range(start,M+1):
        answer.append(i)
        dfs(i)
        answer.pop()


dfs(1)