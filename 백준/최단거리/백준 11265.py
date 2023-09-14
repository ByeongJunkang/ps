# A -> B 일방 통행 존재, But 다른 경우지가 존재할 수 있다.
# C시간 뒤에 B번 파티장에서 새롭게 열리는데, 
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if table[i][j] > table[i][k] + table[k][j]:
                table[i][j] = table[i][k] + table[k][j]

for _ in range(m):
    a,b,c = map(int,input().split())
    if table[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
