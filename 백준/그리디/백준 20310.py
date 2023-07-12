S = list(input())
n,m = 0,0
for i in S:
    if  i == '0':
        n+=1
    else:
        m+=1
num = 0
visited =[False] * len(S)
for i in range(len(S)):
    if num == m//2:
        break

    if S[i] == '1':
        visited[i] = True
        num +=1
num = 0
for i in range(len(S)-1,-1,-1):
    if num == n//2:
        break
    if S[i] == '0':
        visited[i] = True
        num +=1

answer = []
for i in range(len(S)):
    if visited[i] == False:
        answer.append(S[i])

for i in answer:
    print(i,end="")

        
