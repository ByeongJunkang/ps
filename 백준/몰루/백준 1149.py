n = int(input())


k = []
for i in range(n):
    k.append(list(map(int,input().split())))

p= [list(map(int, input().split())) for i in range(n)]
print(p)

  
    
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    print("hi"+ str(i))
    print(p[i][0])
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))