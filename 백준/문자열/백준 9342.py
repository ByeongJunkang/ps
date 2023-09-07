t = int(input())

for _ in range(t):
    a = list(input())
    if ord(a[0]) >= ord('G'):
        print("Good")
        continue
    first,second,third = 0,0,0
    if a[0] == 'A':
        first =1
    flag = True
    for i in range(1,len(a)):
        if a[i] == "A" and first == 0:
            first = 1
            continue
        elif a[i] !="A" and first ==0:
            flag = False
            break
        if first ==1 and second ==0 and third ==0: 
            if a[i] == 'A':
                continue
            elif a[i] =="F":
                second =1
                continue
            else:
                flag = False
                break
        
        elif first == 1 and second == 1 and third == 0:
            if a[i] == 'A':
                continue
            elif a[i] =="F":
                continue
            elif a[i] == "C":
                third = 1
                continue
            else:
                flag = False
                break

        elif first ==1 and second == 1 and third == 1:
            if ord(a[i]) >= ord("G"):
                flag = False
                break
        

    if flag  == True:
        print("Infected!")
    else:
        print("Good")

        