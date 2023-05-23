def find_sqr(s):
    for i in range(N-s+1):
        for j in range(M-s+1):
            if arr[i][j] == arr[i][j+s-1] == arr[i+s-1][j] == arr[i+s-1][j+s-1]:
                return True
    

    return False


answer = 0

N, M = map(int,input().split())

arr = [ list(map(int,input())) for _ in range(N)]

size = min(N,M)
for k in range(size,0,-1):
    if find_sqr(k):
        answer = k ** 2
        break


print(answer)


