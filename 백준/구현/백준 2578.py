Bingo = [list(map(int,input().split())) for _ in range(5)]

answer = [list(map(int,input().split())) for _ in range(5)]


def check():
    Bingo_num =0
    bin_num = True
    for k in range(5):
        if Bingo[k][k] != 0:
            bin_num = False
            break
    if bin_num == True:
        Bingo_num +=1    
    bin_num1 = True
    for k in range(5):
        if Bingo[k][4-k] !=0:
            bin_num1 = False
            break
    if bin_num1 == True:
        Bingo_num+=1
    
    for k in range(5):
        if Bingo[k].count(0) == 5:
            Bingo_num +=1

    
    for k in range(5):
        bin_num2 = True
        for t in range(5):
            if Bingo[t][k] !=0:
                bin_num2 = False
                break
        if bin_num2 == True:
            Bingo_num +=1

    return Bingo_num
count = 0
result = 0
flag = 0
for i in range(5):
    if flag == 1:
        break
    for j in range(5):
        if flag == 1:
            break
        for k in range(5):
            for h in range(5):
                if answer[i][j] == Bingo[k][h]:
                    Bingo[k][h] = 0
                    count +=1
                    break
  
        if count >=12:
            result = check()
            
        if result >=3:
            flag = 1
            break    

print(count)