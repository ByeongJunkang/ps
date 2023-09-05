import sys
a =list(input())
result = []
length = 0
for i in range(len(a)):
    if a[i] == 'X':
        length +=1
    
    elif a[i] =='.':
        ans = length // 4
        res = length % 4
        if res %2 == 1:
            print(-1)
            sys.exit()
            
        else:
            if ans !=0:
                result.append('AAAA'*ans)
            result.append('BB'*(res //2))
        result.append('.')
        length = 0
    
    if a[i] == 'X' and i == len(a) - 1:
        ans = length // 4
        res = length % 4
        if res %2 == 1:
            print(-1)
            sys.exit() 
        else:
            if ans !=0:
                result.append('AAAA'*ans)
            result.append('BB'*(res //2))
            


for a in result:
    print(a,end='')
