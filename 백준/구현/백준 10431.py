p = int(input())
for _ in range(p):
    sum = 0
    num = list(map(int,input().split()))
    temp = num[0]
    for i in range(2,21):
        standard = num[i]
        for j in range(1,i+1):
            if num[j] > standard:
                sum += i -j
                break
        del num[i]
        num.insert(j,standard)
    print(temp,sum)