M ,K= map(int,input().split())
table = list(input())
count = 0



for i in range(len(table)):
    change = False
    if table[i] == 'P':
        for k in range(K,0,-1):
            if i - k >=0:
                if table[i-k] == "H":
                    count +=1
                    table[i-k] = "E"
                    change = True
                    break
        if change == False:
            for k in range(1,K+1):
                if i + k < M:
                    if table[i+k] == "H":
                        count +=1
                        table[i+k] = "E"
                        break

print(count)