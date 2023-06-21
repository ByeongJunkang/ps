N = int(input())
count = 0
for i in range(1,N+1):
    if i < 10:
        count+=1
    
    elif 10 <= i < 100:
        count +=1
    elif 100<=i<1000:
        a = i //100
        b = i %100//10
        c = i % 10
        diff1 = a-b
        diff2 = b-c
        if diff1 == diff2:
            count+=1


print(count)
