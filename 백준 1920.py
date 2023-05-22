N = int(input())

A = list(map(int,input().split()))
A.sort()
M = int(input())
B = list(map(int,input().split()))



def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

   
        if array[mid] == target:
            return array[mid]
      
        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None
    




for i in range(len(B)):
    if binary_search(A,B[i],0,N-1):
        print(1)
    else:
        print(0)
