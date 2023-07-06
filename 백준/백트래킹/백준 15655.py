N,M = map(int,input().split())
num = sorted(list(map(int,input().split())))
result = []
def combi(start):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(start,len(num)):
        result.append(num[i])
        combi(i+1)
        result.pop()

combi(0)