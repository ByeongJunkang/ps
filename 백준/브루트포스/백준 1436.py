
n = int(input())
i = 0
tmp = []
while True:
    a = str(i)
    if "666" in a:
        tmp.append(i)
    
    if len(tmp) == n:
        break
    i+=1
print(tmp[n-1])