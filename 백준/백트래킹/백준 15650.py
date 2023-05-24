import sys
sys.setrecursionlimit(10**7)

M, N = map(int,input().split())
com = set()

arr = [i for i in range(1,M+1)]
def combination(arr,N):

    used = [0 for _ in range(M)]

    def generate(chosen, used):
        
        if len(chosen) == N and tuple(sorted(chosen)) not in com:
            print(*chosen)
            chosen.sort()
            com.add(tuple(chosen))
            return
        
        for i in range(len(arr)):
            if not used[i] :
            
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen,used)
                used[i] = 0
                chosen.pop()


    generate([],used)

combination(arr,N)