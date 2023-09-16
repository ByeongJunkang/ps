from itertools import combinations
t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().split()
    real = []
    for i in mbti:
        if real.count(i) < 3:
            real.append(i)
    ans = 10**9
    for mb in combinations(real,3):
        a,b,c = mb[0],mb[1],mb[2]
        tmp = 0
        for i in range(4):
            if a[i] != b[i]:
                tmp +=1
            if a[i] != c[i]:
                tmp+=1
            if b[i] != c[i]:   
                tmp+=1
        
        ans = min(ans,tmp)
    print(ans)