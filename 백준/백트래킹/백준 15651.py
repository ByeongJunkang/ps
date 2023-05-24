M,N = map(int,input().split())

arr = [i for i in range(1,M+1)]
answer = list()


def dfs(arr,N):

    if len(answer) == N:
        print(*answer)
        return

    for i in range(len(arr)):
        answer.append(arr[i])
        dfs(arr,N)
        answer.pop()

    
dfs(arr,N)
