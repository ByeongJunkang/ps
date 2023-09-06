from collections import defaultdict
N = int(input())
for _ in range(N):
    tmp = list(input())
    a = defaultdict(int)
    for i in tmp:
        if i != ' ':
            a[i] += 1
    b = sorted(a.items(),key= lambda x:x[1],reverse= True)
    if len(b) == 1:
        print(b[0][0])
    else:
        if b[0][1] == b[1][1]:
            print("?")
        else:
            print(b[0][0])
    