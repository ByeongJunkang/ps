from collections import defaultdict
a,b = map(int,input().split())
tmp = defaultdict(str)
for _ in range(a):
    site,pw = input().split()
    tmp[site] = pw

for _ in range(b):
    site = input()
    print(tmp[site])



