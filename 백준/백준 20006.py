# 매칭 가능한 방이 없다면 새로운 방을 생성
# 처음 입장한 플레이어 기준 -10 ~ + 10
# 입장 가능한 방이 있다면, 입장시킨 후 방의 정원이 모두 찰 때까지 대기시킨다.
# 입장 가능한 방이 여러 개라면 먼저 생성된 방에 입장
# 방의 정원이 모두 차면 게임을 시작
p,m = map(int,input().split())
room = [[] for _ in range(p)]
for _ in range(p):
    l,n = input().split()
    
    for i in room:
        if len(i) == 0:
            i.append([l,n])
            break
        elif len(i) < m and  int(i[0][0])-10<=int(l)<=int(i[0][0])+10:
            i.append([l,n])
            break
        else:
            continue

for i in room:
    i.sort(key=lambda x: x[1])

for i in room:
    if len(i)> 0:
        if len(i) == m:
            print("Started!")

        elif len(i)!=0:
            print("Waiting!")

        for j in i:
            print(*j)
                


