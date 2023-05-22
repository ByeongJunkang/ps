S = input()
N = input()


Arr = [[0] * (len(S)+1) for _ in range((len(N)+1))]




for i in range (1,len(N)+1):
    for j in range (1,len(S)+1):
        if N[i-1] == S[j-1]:
            Arr[i][j] = Arr[i-1][j-1]+1
        else:
            Arr[i][j] = max(Arr[i][j-1],Arr[i-1][j])


print(Arr[len(N)][len(S)])