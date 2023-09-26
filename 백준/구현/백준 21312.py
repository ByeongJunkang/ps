from itertools import combinations
tmp= list(map(int,input().split()))
even = []
odd = []
for n in range(1,4):
    combi = list(combinations(tmp,n))
    for i in combi:
        result = 1
        for j in i:
            result *= j
        if result %2 ==1:
            odd.append(result)
        else:
            even.append(result)

odd.sort()
even.sort()
if len(odd) > 0:
    print(odd[-1])
else:
    print(even[-1])

