import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int,input.split()))
num_list = []

for i in range(N):
    if len(num_list) == 0:
        num_list.append(num[i])
    
    left ,right = 0, len(num_list)
    answer = 0
    if num_list[-1] < num[i]:
        num_list.append(num[i])
    else:
        while left <right:
            middle = (left+right) //2
            if num_list[middle] >=num[i]:
                right = middle
            else:
                left = middle+1           
        if num_list[right] >= num[i]:
            num_list[right] = num[i]

print(len(num_list))