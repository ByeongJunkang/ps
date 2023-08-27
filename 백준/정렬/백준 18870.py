import sys
input =sys.stdin.readline
N=int(input())
num_list = list(map(int,input().split()))
num_list1 = sorted(list(set(num_list)))
for i in num_list:
    left =0 
    right = len(num_list1) - 1
    target = i
    while left <= right:
        mid = (left + right ) //2
        if num_list1[mid] < target:
            left = mid + 1
        elif num_list1[mid] == target:
            print(mid, end= " ")
            break
        else:
            right = mid - 1

import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr2 = []

arr2 = list(sorted(set(arr)))

dic = {arr2[i] :i for i in range(len(arr2))}

for i in range(N):
    num = arr[i]
    print(dic[num], end = ' ')