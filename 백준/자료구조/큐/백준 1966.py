t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    num_list = list(map(int,input().split()))
    tmp = [i for i in range(n)]
    cnt = 0
    while True:
        flag = False
        for i in range(1,len(tmp)):
            if num_list[tmp[0]] < num_list[tmp[i]]: 
                flag = True
                break
        if flag == False:
            cnt +=1
            if m == tmp.pop(0):
                print(cnt)
                break
            
        else:
            a = tmp.pop(0)
            tmp.append(a)