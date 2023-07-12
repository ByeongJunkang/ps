T = int(input())
#n = 팀개수
# k = 문제개수
# t 내팀
# m = 로그
for _ in range(T):
    n,k,t,m = map(int,input().split())
    score_list = [[0] * 4 for _ in range(n+1)]
    submit_list = [[0] * (k+1) for _ in range(n+1)]
    num = 0
    for _ in range(m):
        
        #id = 팀_id
        #j = 문제 번호
        #획득한 점수
        id , j,s = map(int,input().split())
    
        submit_list[id][j] = max(submit_list[id][j],s)

        score_list[id][1] += 1
        score_list[id][2] = num
        score_list[id][3] = id
        num +=1
    
    for i in range(1,n+1):
        score_list[i][0] = sum(submit_list[i])
    
    score_list.pop(0)
    score_list.sort(key=lambda x:(-x[0],x[1],x[2]))
    for i in range(n):
        if score_list[i][3] == t:
            print(i+1)
            break
        