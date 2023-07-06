N,M = map(int,input().split())
num = sorted(list(map(int,input().split())))

result = []
def permutation():
    if len(result) == M:
        print(*result)
        return  
    for i,v in enumerate(num):
        if v not in result:
            result.append(v)
            permutation()
            result.pop()
permutation()
