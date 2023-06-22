N = int(input())
budget = list(map(int,input().split()))
limit = int(input())

answer = 0
left, right = 0, max(budget)
while left <= right:
    middle = (left+right)//2
    sum = 0
    for i in range(N):
        if budget[i] >= middle:
            sum += middle
        else:
            sum += budget[i]    
    if sum > limit:
        right = middle -1
    else:
        left = middle + 1
        answer = middle
print(answer)