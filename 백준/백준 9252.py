S = input()
N = input()


Arr = [[0] * (len(S)+1) for _ in range((len(N)+1))]
visited  = [[False] * (len(S)+1) for _ in range((len(N)+1))]



for i in range (1,len(N)+1):
    for j in range (1,len(S)+1):
        if N[i-1] == S[j-1]:
            Arr[i][j] = Arr[i-1][j-1]+1
        else:
            Arr[i][j] = max(Arr[i][j-1],Arr[i-1][j])


L1 = Arr[len(N)][len(S)]







    



cur_x = len(N)
cur_y = len(S) 
count = L1
Answer = ''
while (count > 0):
  
    
    if Arr[cur_x][cur_y] == Arr[cur_x][cur_y-1]:
        cur_y -=1
    elif Arr[cur_x][cur_y] == Arr[cur_x-1][cur_y]:
        cur_x-=1

    elif Arr[cur_x][cur_y] == Arr[cur_x-1][cur_y-1]+1 and Arr[cur_x-1][cur_y] == count-1 and Arr[cur_x][cur_y-1] == count -1:
        Answer= Answer +N[cur_x-1]
        cur_x-=1
        cur_y-=1
        count -=1
       

print(L1)
if L1 != 0:
    print(Answer[::-1])

        

  







