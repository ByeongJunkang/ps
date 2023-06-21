N = int(input())
answer = []
for _ in range(N):
    a,b,c = map(int,input().split())
    answer.append([a,b,c])

count = 0
for num in range(100,1000):
    result1 = list(map(int,str(num)))
    if result1[0] == result1[1] or result1[0] == result1[2] or result1[1] == result1[2]:
        continue
    for j in answer:
        St = 0
        BB = 0
        result = list(map(int,str(j[0])))
        for k in range(3):
            if result1[k] == result[k]:
                St +=1
                result[k] = 0
        for k in range(3):
            if result1[k] in result:
                BB +=1
        
        isTrue = True
        if St != j[1] or BB != j[2]:
            isTrue = False
            break
    
    if isTrue == True and 0 not in result1:
        count +=1

print(count)
