import sys
import math
input  = sys.stdin.readline
n = int(input())

tmp = sorted(list(map(int,input().split())))

if tmp[0] >=0:
    print(tmp[0], tmp[1])
elif tmp[-1] <= 0:
    print(tmp[-2], tmp[-1])

else:
    ans = math.inf
    left ,right = 0,n-1

    result = []
    while left < right:
        if abs(tmp[left]) < abs(tmp[right]):
            ts = abs(tmp[left] + tmp[right])
            if ans > ts:
                result = []
                result.append([tmp[left],tmp[right]])
                ans =ts
            right -=1
        
        elif abs(tmp[left]) > abs(tmp[right]):
            ts = abs(tmp[left] + tmp[right])
            if ans > ts:
                result = []
                result.append([tmp[left],tmp[right]])
                ans = ts
            left+=1

        elif abs(tmp[left]) == abs(tmp[right]):
            print(tmp[left],tmp[right])
            sys.exit()

    print(result[0][0], result[0][1])
