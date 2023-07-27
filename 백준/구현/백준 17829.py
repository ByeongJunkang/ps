N = int(input())

matrix = []

for _ in range(N):
    matrix.append(list(map(int,input().split())))


def split(r,c,N): 
    mid = N//2
    if N ==2:
        answer = [matrix[r][c],matrix[r][c+1],matrix[r+1][c],
                  matrix[r+1][c+1]]
        answer.sort()
        return answer[-2]
    
    ab=split(r,c,mid)
    bc=split(r+mid,c,mid)
    cd=split(r,c+mid,mid)
    de=split(r+mid,c+mid,mid)
    answer = [ab,bc,cd,de]
    answer.sort()
    return answer[-2]

    
print(split(0,0,N))