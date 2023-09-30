n,m = map(int,input().split())
time = n* 60 + m - 45
if time >=0:
    print(time//60, time % 60)
else:
    time += 60 * 24
    print(time//60, time % 60)



