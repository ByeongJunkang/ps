a,b = map(int,input().split())

Z = (b*100) //a

answer = -1
left ,right = 1, 1000000000
while left<=right:
    middle = (left+right)//2
    if ((b+middle) * 100) //(a+middle) > Z:
        right = middle - 1
        answer = middle

    else:
        left = middle +1

print(answer)