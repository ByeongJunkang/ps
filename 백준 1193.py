import sys

n = int(sys.stdin.readline())



sum_count = 0
i = 1
while(sum_count < n):
    sum_count = sum_count + i
    i +=1

j = i -1
start_point = sum_count + 1 - j
diff = n - start_point + 1

   
if j % 2 == 1:
    a = j + 1 - diff
    b = diff
else:
    a = diff
    b = j + 1 - diff

print(str(a)+"/"+str(b))



