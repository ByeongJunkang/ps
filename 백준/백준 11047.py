n, m = map(int,input().split())

Money = [0] * n

for i in range(n):
    Money[i] = int(input())

find_Min = [m // Money[i] for i in range(n) if m  // Money[i]> 0]
num = len(find_Min)
count = 0
while(num > 0):
    count =  count + m // Money[num-1]
    m = m % Money[num-1]
    num = num -1
    if(m == 0):
        break



print(count)

