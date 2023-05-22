N = int(input())

# arr = list()
# for i in range(N):
#     arr = list(map(str,input()))
#     print(arr)


arr = [list(input()) for i in range(N)]



for i in range(N):
   
    Pelindrom = False
    Problem = 0
    length = len(arr[i])
    if arr[i][0] == arr[i][length-1]:
        k = 1
        while k <= (length-k):
            if arr[i][k] == arr[i][length-1-k]:
                Pelindrom = True
            else:
                Pelindrom = False
                break
            k+=1

    if Pelindrom == False:
        Problem = 1
        count = 0
        
        k = 0
        j = length -k-1

        while k <= (length-k):
            if arr[i][k] == arr[i][j]:
                Pelindrom = True
                k+=1 
                j -= 1
            else:
                if arr[i][k+1] == arr[i][j] and count == 0:
                    Pelindrom = True
                    k +=2
                    j-=1
                    count +=1

                elif arr[i][k] == arr[i][j-1] and count == 0:
                    Pelindrom = True
                    count +=1
                    k +=1
                    j-=1
                else:
                    Pelindrom = False
                    Problem = 2
                    break

    if N == 1:
        Pelindrom = True
        print(0)
        break


    print(Problem)
               

