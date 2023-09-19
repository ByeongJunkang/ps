# from itertools import combinations
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     q = list()
#     candidate = set()
#     for _ in range(n):
#        a,b=input().split()
#        q.append([a,b])
#        candidate.add(b)
#     ans = 0
#     for i in range(1,len(candidate)+1):
#         for tmp in combinations(q,i):
#             cate = set()
#             flag = True
#             for k in tmp:
#                 if k[1] in cate:
#                     flag = False
#                     break
#                 else:
#                     cate.add(k[1])
#             if flag:
#                 ans +=1
#     print(ans)

from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    q = defaultdict(list)
    for _ in range(n):
        a,b = input().split()
        q[b].append(a) 
    can = 1
    for tmp in q.keys():
        can *= (len(q[tmp]) + 1)
    print(can-1)
    
    