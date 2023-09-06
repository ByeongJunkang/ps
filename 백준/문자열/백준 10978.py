N = [[-1]* 15 for _ in range(5)]
for i in range(5):
    a= list(input())
    for j in range(len(a)):
        N[i][j] = a[j] 

for a in range(15):
    for b in range(5):
        if N[b][a] != -1:
            print(N[b][a],end='')