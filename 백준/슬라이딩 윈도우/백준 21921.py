N, X = map(int,input().split())
blog = list(map(int,input().split()))
max_num =0
straw_num = 0
days = 1
straw = 1
result = []
for i, v in enumerate(blog):
    if days <= X:
        max_num += v
        days +=1
    else:
        if days == X+1 :
            new_max = max_num
        new_max = new_max - blog[i-X] +v
        if new_max == max_num:
            straw +=1
            result.append(straw)
        elif new_max > max_num:
            straw = 1
            result.append(straw)
        max_num = max(new_max,max_num)
        days +=1
if max_num == 0:
    print("SAD")
else:
    print(max_num)
    print(straw)
        

