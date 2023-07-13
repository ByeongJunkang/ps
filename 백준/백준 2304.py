N = int(input())

roop = []
max_roop = 0
for _ in range(N):
    a,b = map(int,input().split())
    roop.append([a,b])
    max_roop = max(max_roop,b)
    if max_roop == b:
        max_index = a
roop.sort(key=lambda x: x[0])

sum = 0
i = 0
for l in roop :
    if l[1] >sum :
        sum = l[1]
        max_index = i
    i += 1


height = roop[0][1]
for k in range(max_index):
    if height < roop[k+1][1]:
        sum += (roop[k+1][0] - roop[k][0]) *  height
        height = roop[k+1][1]
    else:
        sum += height * (roop[k+1][0] - roop[k][0])

height = roop[-1][1]
for j in range(N-1,max_index,-1):
    if height < roop[j-1][1]:
        sum += (roop[j][0]-roop[j-1][0] ) * height
        height = roop[j-1][1]
    else:
        sum += (roop[j][0]-roop[j-1][0]) * height

print(sum)