n,new,p = map(int,input().split())
if n == 0:
    print(1)

else:
    scores = list(map(int,input().split()))
    scores.sort(reverse=True)
    result = -1
    for i in range(n):
        if scores[i] <= new:
            result = i + 1
            break

    if scores[-1] ==  new and n + 1 > p:
        result= -1
    elif result == -1 and n +1 <=p:
        result = n+1

    print(result)