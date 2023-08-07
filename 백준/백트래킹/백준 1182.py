N,S = map(int,input().split())
num_list = sorted(list(map(int,input().split())))
result = []
answer = 0
def dfs(count,num,sum):
    global answer
    if len(result) == count:
        if sum == S:
            answer +=1
        return
    
    for i in range(num,N):
        result.append(num_list[i])
        dfs(count,i+1,sum+num_list[i])
        result.pop()


for i in range(1,N+1):
    dfs(i,0,0)

print(answer)
    


