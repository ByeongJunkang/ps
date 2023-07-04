N = int(input())
num = list(map(int,input().split()))
add,minus,mul,div = map(int,input().split())
answer = []
def dfs(start,result):
    global add, minus,mul,div
    if start == N:
        answer.append(result)
        return
    if add > 0:
        add -=1
        dfs(start +1, result + num[start])
        add+=1
    if minus > 0:
        minus -=1
        dfs(start +1, result - num[start])
        minus +=1
    if mul > 0:
        mul -=1
        dfs(start+1,result * num[start])
        mul +=1
    if div > 0:
        div -=1
        dfs(start+1,int(result/num[start]))
        div +=1  
dfs(1,num[0])
print(max(answer))
print(min(answer))