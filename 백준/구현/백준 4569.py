import sys
mo = ['a','e','i','o','u']
while True:
    insert = sys.stdin.readline().rstrip()
    if insert == 'end':
        break
    
    flag = 0
    flag1 = 0
    flag2 = 0
    for j in insert:
        for i in mo:
          
            if j == i:
                flag =1
                break
   
    if flag == 0 :
        print("<%s> is not acceptable." %(insert))

    
    elif flag == 1:
        letter = []
        for j in insert:
            if len(letter) > 0:
                if letter[-1] == j and letter[-1] != 'e' and letter[-1] !='o':
                    flag1 = 1
                    print("<%s> is not acceptable." %(insert))
                    break
                

            letter.append(j)
        moja = []
        moum =1
        jaum = 1    
        for j in insert:
            if len(moja) > 0:
                if moja[-1] in mo and j in mo:
                    moum +=1
                elif moja[-1] in mo and j not in mo:
                    moum = 1
                elif moja[-1] not in mo and j not in mo:
                    jaum +=1
                elif moja[-1] not in mo and j in mo:
                    jaum = 1
            moja.append(j)  
            if jaum >=3 or moum >=3:
                flag2= 1
                print("<%s> is not acceptable." %(insert))
                break  
    
    if flag == 1 and flag1 == 0 and flag2 == 0:
        print("<%s> is acceptable." %(insert))


# letter = ""
# letter = letter +  "a"
# print(letter)