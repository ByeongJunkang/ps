M, N = map(int,input().split())


arr = [i for i in range(1,M+1)]


def dfs(arr,N):
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == N:
            print(*chosen)
            return
        
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen,used)
                used[i] = 0
                chosen.pop()

    
    generate([],used)

dfs(arr,N)