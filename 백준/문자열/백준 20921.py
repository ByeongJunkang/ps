from collections import defaultdict
dic = defaultdict(int)
n = int(input())
for _ in range(n):
    a,b = input().split(".")
    dic[b] +=1
a = sorted(dic.items(),key= lambda x: x[0])
for i in a:
    print(i[0], i[1])