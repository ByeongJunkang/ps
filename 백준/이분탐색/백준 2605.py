N, M = map(int,input().split())
trees = list(map(int,input().split()))
left , right = 0, max(trees)
while left<=right:
    middle = (left+right) //2
    cut = 0
    for i in trees:
        if i  > middle:
            cut+= i-middle
    if cut >= M:
        left = middle +1
    else:
        right = middle -1
print(right)