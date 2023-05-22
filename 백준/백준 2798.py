import itertools

n,m = map(int, input().split())
cards = list(map(int, input().split()))
nPr = list(itertools.combinations(cards,3))
Sum = [sum(nPr[i]) - m for i in range(len(nPr)) if sum(nPr[i]) - m <= 0]
print((max(Sum)+m))
