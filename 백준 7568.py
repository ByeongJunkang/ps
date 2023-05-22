m = int(input())


height = list()
weight = list()
ranking = [1] * m
for i in range(m):
    X,Y = map(int,input().split())
    height.append(X)
    weight.append(Y)

for i in range(m):
    for j in range(m):
        if height[i] < height[j] and weight[i] < weight[j]:
            ranking[i] += 1


print(*ranking)
