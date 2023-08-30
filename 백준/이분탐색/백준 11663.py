import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
num = list(map(int,input().split()))
num.sort()
temp = set(num)
def binary_search(left,right,target,dir):
    while left <= right:
        mid = (left + right) //2
        if target < num[mid]:
            right = mid - 1
        elif target > num[mid]:
            left = mid + 1
        else:
            return mid
    if dir == 1:
        return right
    else:
        return left
    

for _ in range(m):
    a,b = map(int,input().rstrip().split())
    left , right = 0, n -1
    a_result = binary_search(left,right,a,0)
    b_result = binary_search(left,right,b,1)
    print(b_result-a_result+1)
        
