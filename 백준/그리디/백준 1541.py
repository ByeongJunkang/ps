a = input().split('-')
result=[]
for i in a:
    tmp = i.split("+")
    sum_num = 0
    for j in tmp:
        sum_num += int(j)
    result.append(sum_num)
ans = result[0]
for i in range(1,len(result)):
    ans -=result[i]
print(ans)
