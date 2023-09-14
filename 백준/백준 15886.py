n = int(input())
loc = list(input())
ans = 1
for i in range(1,n):
    if loc[i] == 'E':
        if loc[i-1] == "W":
            ans+=1
print(ans)