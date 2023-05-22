import sys

Trees = dict()
Total_Trees = 0
while True:
   
    n = sys.stdin.readline().rstrip()
    if n == '':
        break
    
    if n in Trees:
        Trees[n] +=1
    else:
        Trees[n] = 1

    Total_Trees +=1

sdic = dict(sorted(Trees.items()))

for i in sdic:
    a = sdic[i] / Total_Trees * 100

    print("%s %.4f" %(i,a))
