N = int(input())

switch = list(map(int,input().split()))
switch.insert(0,0)

people = []

M = int(input())

for i in range(M):
    student = list(map(int,input().split()))
    people.append(student)

for i in people:
    if i[0] == 1:
        j = 1
        while(j * i[1] <= N):
            if switch[j*i[1]] == 1:
                switch[j*i[1]] = 0
            else:
                switch[j*i[1]] = 1  
            j+=1  
        

    else:
        j = 1
        if switch[i[1]] == 0:
            switch[i[1] ] = 1
        else:
            switch[i[1]] = 0

        while(i[1] - j >= 1 and i[1] + j <= N):
            if switch[i[1]-j] == switch[i[1]+j]:
                if switch[i[1]-j] == 1:
                    switch[i[1]-j] = 0
                else:
                    switch[i[1]-j]= 1
                
                if switch[i[1]+j] == 1:
                    switch[i[1]+j] = 0
                else:
                    switch[i[1]+j] = 1
            else:
                break

            j+=1
        
            

for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()