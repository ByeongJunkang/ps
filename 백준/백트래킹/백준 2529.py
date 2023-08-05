import math
N = int(input())
num = [i for i in range(10)]
deungho = ['']+ input().split()
visited = [0] * 10

max = 0

min = math.inf
result = []
def dfs(i,k):
    
    if  i-1== N:
        result.append(k)
        return

    if deungho[i] == "<":
        for j in range(k%10+1,10):
            if not visited[j]:
                visited[j] = True
                dfs(i+1,k*10 + j)
                visited[j] = False
        
    else:
        for j in range(k%10):
            if not visited[j]:
                visited[j] = True
                dfs(i+1,k*10 + j)
                visited[j] = False


for i in range(0,10):
    visited[i] = True     
    dfs(1,i)
    visited[i] = False

print(result)