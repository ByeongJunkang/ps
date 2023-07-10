n,k = map(int,input().split())
medal = [list(map(int,(input().split()))) for _ in range(n)]
medal.sort(key = lambda x: (-x[1], -x[2],-x[3]))
for i in range(n):
    if medal[i][0] == k:
        a,b,c = medal[i][1],medal[i][2],medal[i][3]

for i in range(n):
    if medal[i][1] == a and medal[i][2] == b and medal[i][3] == c:
        print(i+1)
        break