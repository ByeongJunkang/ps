while True:
    try:
        a,b = input().split()
        prev_idx = -1
        for i in range(len(a)):
            flag = False
            for j in range(prev_idx+1,len(b)):
                if a[i] == b[j]:
                    flag = True
                    prev_idx = j
                    break
            if flag == False:
                break 
        if flag == True:
            print("Yes")
        else:
            print("No")
    except:
        break