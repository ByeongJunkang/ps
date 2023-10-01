n = int(input())
short = set(' ')

def ans(letter):
    for i in letter:
        print(i,end='') 
    print("")
    
for _ in range(n):
    letter = list(input())
    candidiate = []
    for i in range(len(letter)):
        if letter[i] == " ":
            candidiate.append(i+1)
    if len(candidiate) == 0:
        if letter[0].lower() not in short:
            short.add(letter[0].lower())
            letter.insert(0,"[")
            letter.insert(2,"]")
            ans(letter)
            continue
        else:
            for k in range(1,len(letter)):
                if letter[k].lower() not in short:
                    short.add(letter[k].lower())
                    letter.insert(k,"[")
                    letter.insert(k+2,']')
                    break
            ans(letter)
    else:    
        if letter[0].lower() not in short:
            short.add(letter[0].lower())
            letter.insert(0,"[")
            letter.insert(2,"]")
            ans(letter)
        else:
            flag = False
            for idx in candidiate:        
                if letter[idx].lower() not in short:
                    short.add(letter[idx].lower())
                    letter.insert(idx,"[")
                    letter.insert(idx+2,"]")
                    ans(letter)
                    flag = True
                    break
            if not flag:
                for j in range(1,len(letter)):
                    if letter[j].lower() not in short and letter[j]!=' ':
                        short.add(letter[j].lower())
                        letter.insert(j,"[")
                        letter.insert(j+2,']')
                        break
                ans(letter)
